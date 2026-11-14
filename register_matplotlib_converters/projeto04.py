import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# 1. Importar os dados e definir a coluna 'date' como índice, convertendo para datetime
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Limpar os dados removendo os 2,5% superiores e os 2,5% inferiores
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Copiar o dataframe
    df_line = df.copy()

    # Configurar a figura do matplotlib
    fig, ax = plt.subplots(figsize=(15, 5))
    
    # Desenhar o gráfico de linha
    ax.plot(df_line.index, df_line['value'], color='red', linewidth=1)
    
    # Definir títulos e rótulos
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Salvar a imagem e retornar a figura
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copiar o dataframe e extrair ano e mês
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')  # Nome completo do mês

    # Agrupar por ano e mês, calculando a média das visualizações
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Reordenar as colunas para que os meses fiquem em ordem cronológica correta
    months_order = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_grouped = df_grouped.reindex(columns=months_order)

    # Desenhar o gráfico de barras
    fig = df_grouped.plot(kind='bar', figsize=(15, 7), legend=True).get_figure()
    
    # Configurar rótulos e legenda
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=months_order)

    # Salvar a imagem e retornar a figura
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Copiar o dataframe e preparar os dados fornecidos pelo boilerplate
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date] # Nome do mês abreviado (Jan, Feb...)

    # Configurar os subplots adjacentes (1 linha, 2 colunas)
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))

    # Gráfico 1: Year-wise Box Plot (Tendência)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Gráfico 2: Month-wise Box Plot (Sazonalidade)
    # Forçar a ordem cronológica abreviada dos meses para o eixo X
    months_short_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=months_short_order)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Salvar a imagem e retornar a figura
    fig.savefig('box_plot.png')
    return fig