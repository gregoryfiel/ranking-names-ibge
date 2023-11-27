from ranking_program.Item import Item
from . import constants
import unittest
import io
import sys

class FakeIbge():
    def consumir_nomes(self, nome, localidade= None, sexo=None, decada=None):
        if nome == "gregory":
            return constants.nome_sem_parametros
        else:
            return []


class TestItem(unittest.TestCase):
    suppress_text = io.StringIO()
    sys.stdout = suppress_text

    def test_init(self):
        item = Item('gregory')
        self.assertEqual(item.nome, "gregory")
        self.assertEqual(item.localidade, None)
        self.assertEqual(item.decada, None)
        self.assertEqual(item.sexo, None)
    
    def test_nome_vazio(self):
        with self.assertRaises(TypeError):
            Item()
    
    def test_imprimir_frequencia(self):
        item = Item('gregory', frequencia=1, localidade=43, sexo='M', decada=1990)
        self.assertEqual(item.imprimir_frequencia(), print(f"{item.nome:15} | {item.frequencia:15d} | {item.localidade:2} | {item.sexo:1} | {item.decada:3}"))
    
    def test_imprimir_frequencia_completo(self):
        item = Item('gregory', frequencia=1, localidade='BR', sexo='M', decada=1960)
        self.assertEqual(item.imprimir_frequencia(), print(f"{item.nome:15} | {item.frequencia:15d} | {item.localidade:2} | {item.sexo:1} | {item.decada:3}"))

    def test_to_dict(self):
        item = Item('gregory')
        self.assertEqual(item.to_dict(), {'nome': 'gregory', 'frequencia': None, 'localidade': None, 'sexo': None, 'decada': None})

if __name__ == "__main__":
    unittest.main()
