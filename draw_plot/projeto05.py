import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # 1. Importar os dados do arquivo csv
    df = pd.read_csv('epa-sea-level.csv')

    # Extrair as colunas principais
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # 2. Criar o diagrama de dispersão (Scatter Plot)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y, color='blue', alpha=0.5, label='Dados Históricos')

    # 3. Criar a primeira linha de melhor ajuste (usando todos os dados desde 1880)
    res_all = linregress(x, y)
    
    # Criar uma sequência de anos de 1880 até 2050 para projetar a linha
    x_pred1 = pd.Series([i for i in range(1880, 2051)])
    # Equação da reta: y = mx + c
    y_pred1 = res_all.slope * x_pred1 + res_all.intercept
    
    ax.plot(x_pred1, y_pred1, color='red', linestyle='--', label='Ajuste 1880-2050')

    # 4. Criar a segunda linha de melhor ajuste (filtrando dados do ano 2000 em diante)
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    
    res_recent = linregress(x_recent, y_recent)
    
    # Criar uma sequência de anos de 2000 até 2050 para projetar a linha
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = res_recent.slope * x_pred2 + res_recent.intercept
    
    ax.plot(x_pred2, y_pred2, color='green', linestyle='-', label='Ajuste 2000-2050')

    # 5. Adicionar os rótulos dos eixos, título e legenda
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Ajustar limites do eixo x para visualização limpa
    ax.set_xlim(1870, 2060)

    # 6. Salvar a imagem e retornar a figura (Não modifique estas linhas)
    fig.savefig('sea_level_plot.png')
    return fig