import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importar os dados
import os

# Descobre a pasta onde o script projeto03.py está a rodar
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Junta o caminho da pasta com o nome do arquivo CSV
caminho_csv = os.path.join(diretorio_atual, "medical_examination.csv")

# 1. Importar os dados de forma segura
df = pd.read_csv(caminho_csv)
# 2. Adicionar a coluna 'overweight'
# IMC = peso (kg) / [altura (m)]^2. Como a altura está em cm, dividimos por 100.
bmi = df["weight"] / ((df["height"] / 100) ** 2)
df["overweight"] = (bmi > 25).astype(int)

# 3. Normalizar os dados (0 para bom, 1 para ruim)
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


# 4. Desenhar o Gráfico Categórico
def draw_cat_plot():
    # 5. Criar o DataFrame para o gráfico usando pd.melt
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    # 6. Agrupar e reformatar os dados para contar os valores por 'cardio'
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    )

    # 7. Criar o gráfico com sns.catplot()
    fig = sns.catplot(
        x="variable", y="total", hue="value", col="cardio", data=df_cat, kind="bar"
    ).fig

    # 8. Obter a figura de saída (Já feito na linha acima com .fig)
    # 9. Não modifique as próximas duas linhas
    fig.savefig("catplot.png")
    return fig


# 10. Desenhar o Mapa de Calor
def draw_heat_map():
    # 11. Limpar os dados filtrando os percentis e inconsistências de pressão
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 12. Calcular a matriz de correlação
    corr = df_heat.corr()

    # 13. Gerar uma máscara para o triângulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Configurar a figura do matplotlib
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Plotar a matriz de correlação usando sns.heatmap()
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        vmin=-0.1,
        vmax=0.35,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
    )

    # 16. Não modifique as próximas duas linhas
    fig.savefig("heatmap.png")
    return fig


# Executar as funções para gerar os gráficos
draw_cat_plot()
draw_heat_map()
print("Gráficos gerados com sucesso!")
