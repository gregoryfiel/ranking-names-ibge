from ranking_program.IbgeClient import Ibge

class Item():
    """Classe Item que representa um item do ranking, também considerada uma dataclass.

    Métodos:
        __init__(self, nome, localidade, sexo, frequencia): Inicializa a classe.
        imprimir_frequencia(): Imprime a frequência para um nome.
        to_dict(self): Retorna um dicionário com os atributos do item.
    """
    
    def __init__(self, nome, frequencia=None, localidade=None, sexo=None, decada=None):
        self.nome = nome
        self.frequencia = frequencia
        self.localidade = localidade
        self.sexo = sexo
        self.decada = decada
    
    def imprimir_frequencia(self):
        if (self.localidade and self.sexo and self.decada) is not None:
            print(f"{self.nome:15} | {self.frequencia:15d} | {str(self.localidade):2} | {str(self.sexo):1} | {str(self.decada):3}")
        else:
            print(f"{self.nome:15} | {self.frequencia:15d} | {str(self.localidade)} | {str(self.sexo)} | {str(self.decada)}")

    def to_dict(self):
            return {
                "nome": self.nome,
                "frequencia": self.frequencia,
                "localidade": self.localidade,
                "sexo": self.sexo,
                "decada": self.decada
            }
