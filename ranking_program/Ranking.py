from ranking_program.Item import Item
import os
import json
from multiprocessing import Process, Manager, cpu_count
from itertools import product

class Ranking():
    """Classe que obtém o ranking personalizado de nomes, por localidade e sexo.

    Métodos:
        __init__(self, nomes, localidade, sexo, ibge): Inicializa a classe.
        localidade(self): Retorna a localidade.
        localidade(self, value): Define a localidade.
        formatar_decada(self, decada): Formata a década.
        obter_ranking_data(self, nomes): Obtém o ranking.
        consultar_ranking_individual(self, args): Consulta o ranking individual.
        consultar_ranking(self): Consulta o ranking, com o uso de multiprocessamento.
        ordenar_frequencia(self, consulta): Ordena a frequência dos nomes.
        imprimir_ranking(self, lista_de_nomes): Imprime o ranking.
        verifica_pasta(self): Verifica se a pasta existe.
        importar_nomes(self): Importa os nomes do arquivo nomes.json.
        exportar_ranking(self, lista_de_nomes): Exporta o ranking para o arquivo ranking.json.
    """

    def __init__(self, nomes, localidade, sexo, decada, source):
        self.nomes = nomes
        self.ibge = source
        self.localidade = localidade if localidade else ['BR']
        self.sexo = sexo
        self.decada = decada
        self.list_nomes = Manager().list()

    @property
    def nomes(self):
        return self._nomes
    
    @nomes.setter
    def nomes(self, value):
        if value is True:
            self._nomes = self.importar_nomes()
        else:
            self._nomes = ['ranking']

    @property
    def localidade(self):
        return self._localidade
    
    @localidade.setter
    def localidade(self, value):
        localidade_list = []

        for item in value:
            if item is not None and item.isalpha():
                consulta = self.ibge.consumir_estados(item)
                if consulta is not None:
                    localidade_list.append(consulta)
                else:
                    print("localidade inválida, seguindo a consulta com localidade 'BR'")
                    localidade_list.append("BR")
            else:
                localidade_list.append(item)

        self._localidade = localidade_list

    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self, value):
        if value is None:
            self._sexo = ['None']
        else:
            self._sexo = value

    @property
    def decada(self):
        return self._decada
    
    @decada.setter
    def decada(self, value):
        if value is None:
            self._decada = [None]
        else:
            self._decada = value
        
    def formatar_decada(self, decada):
        if decada >= 1930:
            ano_inicial = (decada // 10) * 10
            ano_final = ano_inicial + 10

            return f"[{ano_inicial},{ano_final}["
        else:
            return "1930["
    
    def obter_ranking_data(self, nome, localidade, sexo, decada):
        ranking_data = self.ibge.consumir_nomes(nome, localidade, sexo, decada)

        return ranking_data

    def consultar_ranking_individual(self, args):
        nome, localidade, sexo, decada = args

        if nome == 'ranking':
            ranking = self.obter_ranking_data(nome, localidade, sexo, decada)

            for item in ranking[0]['res']:
                nome = item['nome']
                frequencia = item['frequencia']

                self.list_nomes.append(Item(nome, frequencia=frequencia, localidade=localidade, sexo=sexo, decada=decada))
                    
        else:
            ranking_data = self.obter_ranking_data(nome, localidade, sexo, decada)
            frequencia = 0
            for item in ranking_data:
                if nome.lower() == item['nome'].lower():
                    if decada is None:
                        frequencia += sum(res['frequencia'] for res in item['res'])
                    else:
                        frequencia += sum(res['frequencia'] for res in item['res'] if res['periodo'] == self.formatar_decada(decada))
                            
            self.list_nomes.append(Item(nome, frequencia=frequencia, localidade=localidade, sexo=sexo, decada=decada))
    
    def consultar_ranking(self):
        combinacoes = list(product(self.nomes, self.localidade, self.sexo, self.decada))
        list_processes = []
        process_index = 0

        num_cores = cpu_count()
        for combinacao in combinacoes:
            process = Process(target=self.consultar_ranking_individual, args=(combinacao,))
            list_processes.append(process)
        
        while process_index < len(list_processes):
            batch_processes = []
            while len(batch_processes) < num_cores and process_index < len(list_processes):
                batch_processes.append(list_processes[process_index])
                process_index += 1
            for process in batch_processes:
                process.start()
            for process in batch_processes:
                process.join()
            for process in batch_processes:
                process.close()

    def ordenar_frequencia(self):
        self.list_nomes = sorted(self.list_nomes, key=lambda x: x.frequencia, reverse=True)

        return self.list_nomes
    
    def imprimir_ranking(self):
        print(f"\nResultado da consulta (Nome|Frequência|localidade|sexo|década):")
        print("-" * 63)
        
        for item in self.list_nomes:
            item.imprimir_frequencia()

        print("-" * 63)

    def verifica_pasta(self):
        path = os.path.join("ranking_program", "arquivos_json")
        
        if not os.path.exists(path):
            os.makedirs(path)
        
        return path

    def importar_nomes(self):
        try:
            path = self.verifica_pasta()

            with open(f"{path}/nomes.json", "r") as infile:
                nomes = json.load(infile)

            return nomes
        
        except Exception as e:
            print(f"Erro ao importar nomes.json: {e}, seguindo consulta com o ranking geral.")

    def exportar_ranking(self):
        try:
            path = self.verifica_pasta()
                
            ranking_dict = [item.to_dict() for item in self.list_nomes]
            
            with open(f"{path}/ranking.json", "w") as outfile:
                json.dump(ranking_dict, outfile, indent=4)

            print("Arquivo ranking.json gerado com sucesso!")
        
        except Exception as e:
            print(f"Erro ao gerar arquivo ranking.json: {e}")
