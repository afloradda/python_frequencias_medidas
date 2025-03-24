import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_json("enem_2023.json")

st.title("Visualizador de Análises do ENEM 2023")

st.header("1. Estatísticas Descritivas")

# Cálculo das estatísticas
descriptive_stats = df.describe()
st.write("### Estatísticas Descritivas das Notas do ENEM")
st.dataframe(descriptive_stats)

st.markdown("**Raciocínio:** As estatísticas descritivas nos ajudam a entender a distribuição das notas. Com elas, podemos analisar média, mediana, desvio padrão, valores mínimos e máximos.")