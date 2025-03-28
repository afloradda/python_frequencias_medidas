import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_json("enem_2023.json")

# Título do App
st.title("Análises do ENEM 2023 (Fictiso)")

# Seção do primeiro exercício: Estatísticas descritivas
st.header("Estatísticas Descritivas")

# Cálculo das estatísticas
descriptive_stats = df.describe()
st.write("### Estatísticas Descritivas das Notas do ENEM")
st.dataframe(descriptive_stats)

st.markdown("**Raciocínio:** As estatísticas descritivas nos ajudam a entender a distribuição das notas. Com elas, podemos analisar média, mediana, desvio padrão, valores mínimos e máximos.")

# Seção do terceiro exercício: Amplitude das notas
st.header("1. Amplitude das Notas")

fig, ax = plt.subplots(figsize=(8, 5))  # Criamos a figura e o eixo
ax.bar(["A", "B", "C"], [10, 20, 15])   # Adicionamos um gráfico de barras dentro do eixo
ax.set_title("Gráfico de Exemplo")      # Definimos o título do gráfico
st.pyplot(fig)                          # Exibimos o gráfico no Streamlit

disciplinas = ['Linguagens', 'Ciências humanas', 'Ciências da natureza', 'Matemática', 'Redação']
valores_min = df[disciplinas].min()
valores_max = df[disciplinas].max()

fig, ax = plt.subplots(figsize=(8, 5))
bar_width = 0.4
indices = np.arange(len(disciplinas))

ax.bar(indices - bar_width/2, valores_min, bar_width, label='Mínimo', color='lightblue')
ax.bar(indices + bar_width/2, valores_max, bar_width, label='Máximo', color='blue')

ax.set_xlabel("Disciplinas")
ax.set_ylabel("Notas")
ax.set_title("Valores Mínimos e Máximos das Notas do ENEM")
ax.set_xticks(indices)
ax.set_xticklabels(disciplinas)
ax.legend()

st.pyplot(fig)

st.markdown("**Raciocínio:** O gráfico exibe a variação das notas por disciplina, facilitando a identificação de qual matéria apresenta maior amplitude.")

# Seção do segundo exercício: Gráfico de dispersão
st.header("2. Gráfico de Dispersão")

x_col = st.selectbox("Selecione o eixo X", df.columns[:-1])
y_col = st.selectbox("Selecione o eixo Y", df.columns[:-1])

fig, ax = plt.subplots()
ax.scatter(df[x_col], df[y_col], alpha=0.5)
ax.set_xlabel(x_col)
ax.set_ylabel(y_col)
ax.set_title(f"Dispersão entre {x_col} e {y_col}")
st.pyplot(fig)

st.markdown("**Raciocínio:** O gráfico de dispersão nos permite verificar a relação entre duas variáveis. Se os pontos estiverem alinhados, há correlação entre as notas. Caso contrário, são variáveis independentes.")
