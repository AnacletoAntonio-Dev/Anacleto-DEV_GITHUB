import numpy as np  # type: ignore


def calculate(list_input):
    # Verifica se a lista tem exatamente 9 elementos
    if len(list_input) != 9:
        raise ValueError("A lista deve conter nove números.")
    
    # Converte a lista em uma matriz 3x3 do NumPy
    matrix = np.array(list_input).reshape(3, 3)
    
    # Cria o dicionário com os cálculos requisitados
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),    # Média das colunas
            matrix.mean(axis=1).tolist(),    # Média das linhas
            matrix.mean().tolist()           # Média da matriz nivelada
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }

    return calculations
from pprint import pprint

# Lista de teste
lista_teste = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Chama a função
resultado = calculate(lista_teste)

# Mostra na tela de forma super organizada
print("--- RESULTADO DOS CÁLCULOS ---")
pprint(resultado)