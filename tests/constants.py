from unittest.mock import MagicMock
import json

"""Este módulo contém as constantes utilizadas nos testes do programa Ranking."""

nome_sem_parametros = [{"nome":"GREGORY","sexo":None,"localidade":"BR",
                        "res":[{"periodo":"[1960,1970[","frequencia":31},
                               {"periodo":"[1970,1980[","frequencia":56},
                               {"periodo":"[1980,1990[","frequencia":614},
                               {"periodo":"[1990,2000[","frequencia":1384},
                               {"periodo":"[2000,2010[","frequencia":1112}]}]

nome_sem_parametros_str = json.dumps(nome_sem_parametros)

nome_invalido = []

nome_com_localidade = [{"nome":"GREGORY","sexo":None,"localidade":"43",
                        "res":[{"periodo":"[1980,1990[","frequencia":94},
                               {"periodo":"[1990,2000[","frequencia":270},
                               {"periodo":"[2000,2010[","frequencia":293}]}]

nome_com_sexo = [{"nome":"GREGORY","sexo":"M","localidade":"BR",
                  "res":[{"periodo":"[1960,1970[","frequencia":31},
                         {"periodo":"[1970,1980[","frequencia":56},
                         {"periodo":"[1980,1990[","frequencia":609},
                         {"periodo":"[1990,2000[","frequencia":1378},
                         {"periodo":"[2000,2010[","frequencia":1104}]}]

nome_com_localidade_sexo = [{"nome":"GREGORY","sexo":"M","localidade":"43",
                             "res":[{"periodo":"[1980,1990[","frequencia":93},
                                    {"periodo":"[1990,2000[","frequencia":270},
                                    {"periodo":"[2000,2010[","frequencia":291}]}]

nome_com_localidade_numeral_invalida = []

nome_com_localidade_alfabeto = [{"nome":"GREGORY","sexo":None,"localidade":"BR",
                                 "res":[{"periodo":"[1960,1970[","frequencia":31},
                                        {"periodo":"[1970,1980[","frequencia":56},
                                        {"periodo":"[1980,1990[","frequencia":614},
                                        {"periodo":"[1990,2000[","frequencia":1384},
                                        {"periodo":"[2000,2010[","frequencia":1112}]}]

nome_com_sexo_invalido = [{"nome":"GREGORY","sexo":None,"localidade":"BR",
                           "res":[{"periodo":"[1960,1970[","frequencia":31},
                                  {"periodo":"[1970,1980[","frequencia":56},
                                  {"periodo":"[1980,1990[","frequencia":614},
                                  {"periodo":"[1990,2000[","frequencia":1384},
                                  {"periodo":"[2000,2010[","frequencia":1112}]}]

siglas_estados = [{"id":43,"sigla":"RS","nome":"Rio Grande do Sul","regiao":{"id":4,"sigla":"S","nome":"Sul"}}]

ranking_geral = [{"localidade":"BR","sexo":None,"res":[{"nome":"MARIA","frequencia":11734129,"ranking":1},
                                                       {"nome":"JOSE","frequencia":5754529,"ranking":2},
                                                       {"nome":"ANA","frequencia":3089858,"ranking":3},
                                                       {"nome":"JOAO","frequencia":2984119,"ranking":4},
                                                       {"nome":"ANTONIO","frequencia":2576348,"ranking":5},
                                                       {"nome":"FRANCISCO","frequencia":1772197,"ranking":6},
                                                       {"nome":"CARLOS","frequencia":1489191,"ranking":7},
                                                       {"nome":"PAULO","frequencia":1423262,"ranking":8},
                                                       {"nome":"PEDRO","frequencia":1219605,"ranking":9},
                                                       {"nome":"LUCAS","frequencia":1127310,"ranking":10},
                                                       {"nome":"LUIZ","frequencia":1107792,"ranking":11},
                                                       {"nome":"MARCOS","frequencia":1106165,"ranking":12},
                                                       {"nome":"LUIS","frequencia":935905,"ranking":13},
                                                       {"nome":"GABRIEL","frequencia":932449,"ranking":14},
                                                       {"nome":"RAFAEL","frequencia":821638,"ranking":15},
                                                       {"nome":"FRANCISCA","frequencia":725642,"ranking":16},
                                                       {"nome":"DANIEL","frequencia":711338,"ranking":17},
                                                       {"nome":"MARCELO","frequencia":693215,"ranking":18},
                                                       {"nome":"BRUNO","frequencia":668217,"ranking":19},
                                                       {"nome":"EDUARDO","frequencia":632664,"ranking":20}]}]

ranking_com_decada = [{"localidade":"BR","sexo":None,"res":[{"nome":"MARIA","frequencia":1487042,"ranking":1},
                                                            {"nome":"JOSE","frequencia":648754,"ranking":2},
                                                            {"nome":"ANTONIO","frequencia":314375,"ranking":3},
                                                            {"nome":"JOAO","frequencia":256001,"ranking":4},
                                                            {"nome":"FRANCISCO","frequencia":160721,"ranking":5},
                                                            {"nome":"ANA","frequencia":101259,"ranking":6},
                                                            {"nome":"MANOEL","frequencia":95014,"ranking":7},
                                                            {"nome":"FRANCISCA","frequencia":91799,"ranking":8},
                                                            {"nome":"PEDRO","frequencia":86926,"ranking":9},
                                                            {"nome":"SEBASTIAO","frequencia":84668,"ranking":10},
                                                            {"nome":"RAIMUNDO","frequencia":80134,"ranking":11},
                                                            {"nome":"LUIZ","frequencia":74213,"ranking":12},
                                                            {"nome":"ANTONIA","frequencia":72229,"ranking":13},
                                                            {"nome":"TEREZINHA","frequencia":65194,"ranking":14},
                                                            {"nome":"JOSEFA","frequencia":61101,"ranking":15},
                                                            {"nome":"PAULO","frequencia":60073,"ranking":16},
                                                            {"nome":"GERALDO","frequencia":56005,"ranking":17},
                                                            {"nome":"CARLOS","frequencia":53410,"ranking":18},
                                                            {"nome":"RAIMUNDA","frequencia":50089,"ranking":19},
                                                            {"nome":"LUIS","frequencia":48056,"ranking":20}]}]

ranking_com_decada_invalida = []

fake_to_dict = {"nome": "GREGORY", "frequencia": 3197, "localidade": None, "sexo": None, "decada": None}

FakeItem1 = MagicMock()
FakeItem1.nome = "GREGORY"
FakeItem1.frequencia = 3197

FakeItem2 = MagicMock()
FakeItem2.nome = "MARA"
FakeItem2.frequencia = 88918

FakeItem3 = MagicMock()
FakeItem3.nome = "MARCELO"
FakeItem3.frequencia = 693215

fake_dict = {
            'key1': 'value1',
            'key2': {
                'nested_key': 'nested_value'
            }
        }

fake_dict2 = {
            'key1': 'value1',
            'key2': {
                'nested_key': set([1, 2, 3])
            }
        }

nomes_json = json.dumps(['gregory', 'mara', 'marcelo'])
