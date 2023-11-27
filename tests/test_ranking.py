import unittest
from unittest.mock import MagicMock, patch
from ranking_program.Ranking import Ranking
from . import constants

class FakeIbge():

    def consumir_nomes(self, nome, localidade= None, sexo=None, decada=None):
        if nome == "gregory":
            return constants.nome_sem_parametros
        elif nome == 'ranking':
            if localidade == None:
                return constants.ranking_geral
            else:
                return []
        else:
            return []

    def consumir_estados(self, localidade):
        if localidade == 'RS' or localidade == '43':
            return constants.siglas_estados[0]['id']
        else:
            return None
      

class TesteRanking(unittest.TestCase):
    def test_init(self):
        ranking = Ranking(False, None, None, None, FakeIbge())
        self.assertEqual(ranking.nomes, ['ranking'])
        self.assertEqual(ranking.localidade, ['BR'])
        self.assertEqual(ranking.sexo, ['None'])
        self.assertEqual(ranking.decada, [None])  
        self.assertIsInstance(ranking.ibge, FakeIbge)
        self.list_nomes = []
    
    @patch('ranking_program.Ranking.Ranking.importar_nomes')
    def test_nomes_get(self, mock_importar_nomes):
        mock_importar_nomes.return_value = ['gregory']
        ranking = Ranking(True, None, None, None, FakeIbge())

        mock_importar_nomes.assert_called_once()
        self.assertEqual(ranking.nomes, ['gregory'])
        
    def test_localidade_get(self):
        ranking = Ranking(True, None, None, None, FakeIbge())
        self.assertEqual(ranking.localidade, ['BR'])

    def test_localidade_set(self):
            ranking = Ranking(True,[ 'RS'], None, None, FakeIbge())
            self.assertEqual(ranking.localidade, [43])

    def test_localidade_invalida(self):
        ranking = Ranking(True, ['XX'], None, None, FakeIbge())
        self.assertEqual(ranking.localidade, ['BR'])

    def test_formatar_decada(self):
        ranking = Ranking(True, None, None, None, FakeIbge())
        self.assertEqual(ranking.formatar_decada(1960), "[1960,1970[")
    
    def test_formatar_decada1920(self):
        ranking = Ranking(True, None, None, None, FakeIbge())
        self.assertEqual(ranking.formatar_decada(1920), "1930[")

    def test_obter_ranking_data(self):
        ranking = Ranking(True, None, None, None, FakeIbge())
        self.assertEqual(ranking.obter_ranking_data('gregory', None, None, None), constants.nome_sem_parametros)

    @patch('ranking_program.Ranking.Ranking.importar_nomes')
    @patch('ranking_program.Ranking.Ranking.obter_ranking_data')
    def test_consultar_ranking_individual(self, mock_obter_ranking_data, mock_importar_nomes):
        mock_importar_nomes.return_value = ['gregory']
        mock_obter_ranking_data.return_value = constants.nome_sem_parametros
        ranking = Ranking(True, None, None, None, FakeIbge())
        ranking.consultar_ranking_individual(('gregory', None, None, None))

        mock_obter_ranking_data.assert_called_once()

    @patch('ranking_program.Ranking.Ranking.obter_ranking_data')
    def test_consultar_ranking_individual_geral(self, mock_obter_ranking_data):
        args = ['ranking', None, None, None]
        mock_obter_ranking_data.return_value = constants.ranking_geral
        ranking = Ranking(True, None, None, None, FakeIbge())
        ranking.consultar_ranking_individual(args)

        mock_obter_ranking_data.assert_called_once()

    @patch('ranking_program.Ranking.Ranking.consultar_ranking_individual')
    @patch('ranking_program.Ranking.Process')
    def test_consultar_ranking(self, mock_process, mock_consultar_ranking_individual):
        mock_consultar_ranking_individual.return_value = None
        ranking = Ranking(True, None, None, None, FakeIbge())
        ranking.consultar_ranking()

        mock_process.assert_called()

    @patch('ranking_program.Ranking.Ranking.importar_nomes')
    def test_ordenar_frequencia(self, mock_importar_nomes):
        mock_importar_nomes.return_value = ['mara','marcelo','gregory']
        ranking = Ranking(True, None, None, None, FakeIbge())
        ranking.list_nomes = [constants.FakeItem1, constants.FakeItem2, constants.FakeItem3]
        ranking.ordenar_frequencia()

        self.assertListEqual(ranking.ordenar_frequencia(), [constants.FakeItem3,  constants.FakeItem2, constants.FakeItem1,])

    @patch('ranking_program.Ranking.Ranking.importar_nomes')
    def test_imprimir_ranking(self, mock_importar_nomes):
        mock_importar_nomes.return_value = ['mara','marcelo','gregory']
        ranking = Ranking(True, None, None, None, FakeIbge())
        ranking.list_nomes = [constants.FakeItem1, constants.FakeItem2, constants.FakeItem3]
        resultado = ranking.imprimir_ranking()
        
        self.assertIsNone(resultado)
    
    @patch('ranking_program.Ranking.Ranking.importar_nomes')
    @patch('builtins.open')
    def test_importar_nomes_exception(self, mock_open, mock_importar_nomes):
        mock_importar_nomes.side_effect = Exception
        mock_open.side_effect = Exception

        with self.assertRaises(Exception):
            ranking = Ranking(True, None, None, None, FakeIbge())
            ranking.importar_nomes()

    @patch('ranking_program.Ranking.json.dump')
    def test_exportar_ranking(self, mock_json_dump):
        ranking = Ranking(True, None, None, None, FakeIbge())
        ranking.exportar_ranking()

        mock_json_dump.assert_called_once()

    @patch('ranking_program.Ranking.Ranking.exportar_ranking')
    def test_exportar_ranking_exception(self, mocK_exportar_ranking):
        mocK_exportar_ranking.side_effect = Exception

        with self.assertRaises(Exception):
            ranking = Ranking(True, None, None, None, FakeIbge())
            ranking.exportar_ranking()

if __name__ == "__main__":
    unittest.main()
