import argparse
from ranking_program.IbgeClient import Ibge, Cache
from ranking_program.Ranking import Ranking
import time


def main():
    """Consulta nomes na API do IBGE e exibe as frequências associadas a cada nome.
       e o ranking geral e específico dos nomes.

    Argumentos:
    --nome -> caso a flag seja passada, o programa irá consultar os nomes no arquivo nomes.json, caso contrário, o programa irá retornar o ranking geral.
    --ranking (str) Nome(s)
    --localidade (int) Localidade
    --decada (int) Década
    --sexo (str) Sexo
    --retryTimeout (int) Número de tentativas e tempo limite para cada tentativa consecutiva
    """
    start_time = time.time()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--nome", action="store_true", default=False,
                        help="Nome(s) para consultar na API do IBGE")
    parser.add_argument("--localidade", nargs="*", type=str,
                        help="Ranking para uma localidade específica")
    parser.add_argument("--sexo", nargs="*", choices=['M', 'F'],
                        help="Ranking para um sexo específico")
    parser.add_argument("--decada", nargs="*", type=int,
                        help="Ranking para uma década específica")
    parser.add_argument("--retryTimeout", nargs=2, type=float, default=[3, 5],
                    help="Número de tentativas e tempo limite para cada tentativa nesta ordem")

    args = parser.parse_args()


    try:
        ibge = Ibge(retry=args.retryTimeout[0], timeout=args.retryTimeout[1])
        ranking = Ranking(args.nome, args.localidade, args.sexo, args.decada, ibge)
        ranking.consultar_ranking()
        ranking.ordenar_frequencia()
        ranking.imprimir_ranking()
        ranking.exportar_ranking()

        end_time = time.time()
        total_time = end_time - start_time
        print(f"Tempo de execução: {round(total_time, 2)} segundos.")

    except Exception as e:
        print(f"Erro: {e.args[0]}.")


if __name__ == "__main__":
    main()
