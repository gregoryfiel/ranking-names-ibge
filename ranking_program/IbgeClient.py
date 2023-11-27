import logging
import requests
from requests.adapters import HTTPAdapter, Retry
import redis
import json
from collections.abc import MutableMapping


class Ibge():
    """Classe Ibge que consome a API do IBGE e gera um documento JSON.
    
    Metodos:
        __init__(self, nome, localidade, sexo, retry, timeout): Inicializa a classe.
        conectar_api(self, url): Método para consultar a API do IBGE e retorna um documento JSON.
        consumir_nomes(self, nome, localidade=None, sexo=None, decada=None): Consulta o cache ou a API do IBGE e retorna um documento JSON.
        consulta_estados(self, estado): Consulta a API do IBGE para estados e retorna o id do estado.
    """

    def __init__(self, retry=3, timeout=5):
        logging.basicConfig(format='%(asctime)s - %(levelname)s:%(message)s')
        self.retry = retry
        self.timeout = timeout
        self.__url = "https://servicodados.ibge.gov.br/api/"
        self.cache_printed = False

    def configuraSession(self):
        self.session = requests.Session()
        retries = Retry(total=self.retry,
                        backoff_factor=0.1,
                        status_forcelist=[502, 503, 504])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
            
    def get_api(self, url, params=None):
        self.configuraSession()
        try:
            response = self.session.get(url,
                                        timeout=self.timeout,
                                        params=params)
            
            response.raise_for_status()
            json_data = response.json()

            return json_data

        except Exception as e:
            logging.error(f"erro durante a solicitação HTTP: {str(e)}")
            raise

    def consumir_nomes(self, nome, localidade=None, sexo=None, decada=None):
        chave = f"{nome}:{localidade}:{sexo}:{decada}"
        try:
            r = Cache()
            data = r.get_json(chave)
            if data:
                return data
            
            else:
                url = f"{self.__url}v2/censos/nomes/{nome}"
                params = {"localidade": localidade, "sexo": sexo, "decada": decada}
                data = self.get_api(url, params)
                r.set_json(chave, data)

                return data
            
        except Exception as e:
            if not self.cache_printed:
                print(f"{e} Seguindo a consulta sem cache.")
                self.cache_printed = True

            url = f"{self.__url}v2/censos/nomes/{nome}"
            params = {"localidade": localidade, "sexo": sexo, "decada": decada}
            data = self.get_api(url, params)

            return data

    def consumir_estados(self, localidade):
            url = self.__url + "v1/localidades/estados"

            api_data = self.get_api(url)
            for item in api_data:
                if item['sigla'] == localidade:
                    return item['id']


class Cache():
    """Classe Cache que armazena os dados em cache.

    Métodos:
        __init__(self, redis_expire=300): Inicializa a classe, com valor padrão de 300 segundos para expiração.
        set_json(self, key, value): Armazena os dados em cache.
        get_json(self, key): Obtém os dados em cache.
        setflat_skeys(self, r, obj: dict, prefix: str, delim: str = ":", *, _autopfix=""): Método auxiliar para armazenar os dados em cache.
    """
    def __init__(self):
        self.redis_host = 'localhost'
        self.redis_port = 6379
        self.redis_password = ''
        self.redis_expiration = 300
        
        self.client = redis.Redis(
            host=self.redis_host,
            port=self.redis_port,
            password=self.redis_password
        )

    def set_json(self, key, value):
        self.setflat_skeys(self.client, {key: value}, prefix="cache", delim=":")

    def get_json(self, key):
        json_string = self.client.get(f"cache:{key}")

        if json_string is None:
            return None
        else:
            return json.loads(json_string)

    def setflat_skeys(
        self, client,
        obj: dict,
        prefix: str,
        delim: str = ":",
        *,
        _autopfix=""
    ) -> None:
        allowed_vtypes = (str, bytes, float, int, list)

        for key, value in obj.items():
            key = _autopfix + key

            if isinstance(value, allowed_vtypes):
                client.set(f"{prefix}{delim}{key}", json.dumps(value), ex=self.redis_expiration)

            elif isinstance(value, MutableMapping):
                self.setflat_skeys(client, value, prefix, delim, _autopfix=f"{key}{delim}")

            else:
                raise TypeError(f"Tipo de valor não suportado: {type(value)}")
