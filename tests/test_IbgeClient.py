import unittest
from unittest.mock import MagicMock, patch
from ranking_program.IbgeClient import Ibge, Cache
from . import constants


class TestIbgeClient(unittest.TestCase):

    def setUp(self):
        self.ibge = Ibge()

    def test_init(self):
        self.assertEqual(self.ibge.retry, 3)
        self.assertEqual(self.ibge.timeout, 5)
    
    @patch('ranking_program.IbgeClient.requests.Session')
    def test_configuraSession(self, mock_session):
        self.ibge.configuraSession()
        mock_session.assert_called_once()

    @patch('ranking_program.IbgeClient.requests.Session.get')
    def test_get_api(self, mock_session):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = constants.ranking_geral
        
        mock_session.return_value = mock_response
        
        url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking'
        response = self.ibge.get_api(url)
        
        mock_session.assert_called_once_with(url, timeout=5, params=None)
        
        self.assertEqual(response, constants.ranking_geral)

    @patch('ranking_program.IbgeClient.requests.Session.get')
    def test_get_api_exception(self, mock_session):
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception('erro teste')

        mock_session.return_value = mock_response

        url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking'

        with self.assertRaises(Exception):
            self.ibge.get_api(url)

    @patch('ranking_program.IbgeClient.Cache')
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_nomes(self, mock_get_api, mock_cache):
        mock_cache.side_effect = ConnectionRefusedError('')
        mock_get_api.return_value = constants.nome_sem_parametros

        response = self.ibge.consumir_nomes('gregory')
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v2/censos/nomes/gregory",
                                             {"localidade": None, "sexo": None, "decada": None})
        
        self.assertEqual(response, constants.nome_sem_parametros)
        
    @patch('ranking_program.IbgeClient.Cache')
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_nomes_nome_invalido(self, mock_get_api, mock_cache):
        mock_cache.side_effect = ConnectionRefusedError('')
        mock_get_api.return_value = constants.nome_invalido

        response = self.ibge.consumir_nomes('facebookerson')
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v2/censos/nomes/facebookerson",
                                             {"localidade": None, "sexo": None, "decada": None})
        
        self.assertEqual(response, constants.nome_invalido)

    @patch('ranking_program.IbgeClient.Cache')
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_nome_com_localidade(self, mock_get_api, mock_cache):
        mock_cache.side_effect = ConnectionRefusedError('')
        mock_get_api.return_value = constants.nome_com_localidade

        response = self.ibge.consumir_nomes('gregory', '43')
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v2/censos/nomes/gregory",
                                             {"localidade": '43', "sexo": None, "decada": None})
        
        self.assertEqual(response, constants.nome_com_localidade)

    @patch('ranking_program.IbgeClient.Cache')
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_nome_com_sexo(self, mock_get_api, mock_cache):
        mock_cache.side_effect = ConnectionRefusedError('')
        mock_get_api.return_value = constants.nome_com_sexo

        response = self.ibge.consumir_nomes('gregory', sexo='M')
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v2/censos/nomes/gregory",
                                             {"localidade": None, "sexo": 'M', "decada": None})
        
        self.assertEqual(response, constants.nome_com_sexo)

    @patch('ranking_program.IbgeClient.Cache')
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_nome_com_localidade_e_sexo(self, mock_get_api, mock_cache):
        mock_cache.side_effect = ConnectionRefusedError('')
        mock_get_api.return_value = constants.nome_com_localidade_sexo

        response = self.ibge.consumir_nomes('gregory', '43', 'M')
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v2/censos/nomes/gregory",
                                             {"localidade": '43', "sexo": 'M', "decada": None})
        
        self.assertEqual(response, constants.nome_com_localidade_sexo)

    @patch('ranking_program.IbgeClient.Cache')
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_nome_localidade_numeral_invalida(self, mock_get_api, mock_cache):
        mock_cache.side_effect = ConnectionRefusedError('')
        mock_get_api.return_value = constants.nome_com_localidade_numeral_invalida

        response = self.ibge.consumir_nomes('gregory', '123456789')
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v2/censos/nomes/gregory",
                                             {"localidade": '123456789', "sexo": None, "decada": None})
        
        self.assertEqual(response, constants.nome_com_localidade_numeral_invalida)

    @patch('ranking_program.IbgeClient.Cache')
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_nome_localidade_alfabeto_invalido(self, mock_get_api, mock_cache):
        mock_cache.side_effect = ConnectionRefusedError('')
        mock_get_api.return_value = constants.nome_com_localidade_alfabeto

        response = self.ibge.consumir_nomes('gregory', 'AX')
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v2/censos/nomes/gregory",
                                             {"localidade": 'AX', "sexo": None, "decada": None})
        
        self.assertEqual(response, constants.nome_com_localidade_alfabeto)

    @patch('ranking_program.IbgeClient.Cache')
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_nome_sexo_invalido(self, mock_get_api, mock_cache):
        mock_cache.side_effect = ConnectionRefusedError('')
        mock_get_api.return_value = constants.nome_com_sexo_invalido

        response = self.ibge.consumir_nomes('gregory', sexo='X')
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v2/censos/nomes/gregory",
                                             {"localidade": None, "sexo": 'X', "decada": None})
        
        self.assertEqual(response, constants.nome_com_sexo_invalido)
    
    @patch('ranking_program.IbgeClient.Cache')
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_nome_ranking_decada(self, mock_get_api, mock_cache):
        mock_cache.side_effect = ConnectionRefusedError('')
        mock_get_api.return_value = constants.ranking_com_decada

        response = self.ibge.consumir_nomes('ranking', decada=1950)
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking",
                                             {"localidade": None, "sexo": None, "decada": 1950})
        
        self.assertEqual(response, constants.ranking_com_decada)

    @patch('ranking_program.IbgeClient.Cache')
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_nome_ranking_decada(self, mock_get_api, mock_cache):
        mock_cache.side_effect = ConnectionRefusedError('')
        mock_get_api.return_value = constants.ranking_com_decada_invalida

        response = self.ibge.consumir_nomes('ranking', decada=2030)
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking",
                                             {"localidade": None, "sexo": None, "decada": 2030})
        
        self.assertEqual(response, constants.ranking_com_decada_invalida)

    @patch('ranking_program.IbgeClient.Cache.get_json')
    def test_consumir_nome_cache(self, mock_cache):
        mock_cache.return_value = constants.nome_sem_parametros

        response = self.ibge.consumir_nomes('gregory')
        mock_cache.assert_called_once()
        
        self.assertEqual(response, constants.nome_sem_parametros)

    @patch('ranking_program.IbgeClient.Cache.set_json')
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    @patch('ranking_program.IbgeClient.Cache.get_json')
    def test_consumir_nome_set_cache(self, mock_cache, mock_get_api, mock_set_json):
        mock_cache.return_value = None
        mock_get_api.return_value = constants.nome_sem_parametros

        response = self.ibge.consumir_nomes('gregory')
        mock_cache.assert_called_once()
        mock_get_api.assert_called_once()
        mock_set_json.assert_called_once()
        
        self.assertEqual(response, constants.nome_sem_parametros)

    @patch('ranking_program.IbgeClient.Ibge.get_api')
    @patch('ranking_program.IbgeClient.Cache')
    def test_consumir_nome_sem_conexão_cache(self, mock_cache, mock_get_api):
        mock_cache.side_effect = ConnectionRefusedError('')
        mock_get_api.return_value = constants.nome_sem_parametros

        response = self.ibge.consumir_nomes('gregory')
        mock_cache.assert_called_once()
        
        self.assertEqual(response, constants.nome_sem_parametros)

    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_estados(self, mock_get_api):
        mock_get_api.return_value = constants.siglas_estados

        response = self.ibge.consumir_estados('RS')
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
        
        self.assertEqual(response, 43)
    
    @patch('ranking_program.IbgeClient.Ibge.get_api')
    def test_consumir_estados_localidade_invalida(self, mock_get_api):
        mock_get_api.return_value = constants.siglas_estados

        response = self.ibge.consumir_estados('XX')
        mock_get_api.assert_called_once_with("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
        
        self.assertEqual(response, None)

class TestCache(unittest.TestCase):
    @patch('ranking_program.IbgeClient.redis.Redis')
    def test_init(self, mock_redis):
        mock_redis.ping.return_value = True
        Cache()
        mock_redis.assert_called_once_with(host='localhost', port=6379, password='')

    @patch('ranking_program.IbgeClient.redis.Redis')
    def test_set_json(self, mock_redis):
        r = Cache()
        r.set_json('gregory:None:None:None', constants.nome_sem_parametros)

        mock_redis.assert_called_once()

    @patch('ranking_program.IbgeClient.redis.Redis.get')
    def test_get_json(self, mock_redis_get):
        mock_redis_get.return_value = constants.nome_sem_parametros_str
        r = Cache()
        get_json = r.get_json('gregory:None:None:None')

        mock_redis_get.assert_called_once()
        self.assertEqual(get_json, constants.nome_sem_parametros)

    @patch('ranking_program.IbgeClient.redis.Redis.get')
    def test_get_json_none(self, mock_get_json):
        mock_get_json.return_value = None

        r = Cache()
        get_json = r.get_json('facebookerson:None:None:None')
        mock_get_json.assert_called_once()

        self.assertEqual(get_json, None)

    @patch('ranking_program.IbgeClient.redis.Redis')
    @patch('ranking_program.IbgeClient.Cache.setflat_skeys')
    def test_setflat_skeys(self, mock_setflat_skeys, mock_redis):
        cache = Cache()
        cache.setflat_skeys(mock_redis, constants.fake_dict, 'prefix', ':')

        mock_setflat_skeys.assert_called_once()

    @patch('ranking_program.IbgeClient.redis.Redis')
    def test_type_error(self, mock_redis):
        with self.assertRaises(TypeError):
            r = Cache()
            r.set_json('gregory:None:None:None', constants.FakeItem2)

if __name__ == "__main__":
    unittest.main()
