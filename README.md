# Desafio de Data Analytics - ENEM 2023

## 📌 Sobre o Projeto
Este repositório contém a análise de um conjunto de dados fictício baseado no ENEM 2023, com foco no desenvolvimento de habilidades em **Data Analytics** utilizando **Python** e bibliotecas de análise de dados.

A solução implementada visa responder questões estatísticas e explorar visualizações para melhor compreensão das informações. O projeto foi estruturado para rodar em um **dashboard interativo** utilizando **Streamlit**.

---
## 🛠️ Ferramentas Utilizadas
- **Python 3.x** → Linguagem principal para manipulação dos dados.
- **Pandas** → Manipulação e análise de dados tabulares.
- **NumPy** → Operações matemáticas e estatísticas.
- **Matplotlib & Seaborn** → Criação de visualizações gráficas.
- **Streamlit** → Construção da interface interativa.

---
## 📊 Estrutura dos Dados
O conjunto de dados contém **1000 registros**, cada um representando um estudante que realizou o ENEM. As colunas incluem:
- **Redação**
- **Matemática e suas Tecnologias**
- **Linguagens, Códigos e suas Tecnologias**
- **Ciências Humanas e suas Tecnologias**
- **Ciências da Natureza e suas Tecnologias**
- **Gênero**

---
## 📌 Questões Resolvidas

### 1️⃣ Maior amplitude entre as disciplinas
- Conceito abordado: **Amplitude estatística** (diferença entre o maior e o menor valor).
- Método: Utilização de `max()` e `min()` em cada disciplina.

### 2️⃣ Média e Mediana das disciplinas
- Conceito abordado: **Tendências centrais (média vs mediana)**.
- Método: Uso de `mean()` para média e `median()` para mediana, excluindo valores nulos.

### 3️⃣ Desvio padrão e média ponderada dos 500 melhores
- Conceito abordado: **Peso nas disciplinas e dispersão dos dados (desvio padrão)**.
- Método: Cálculo de média ponderada seguido de `std()`.

### 4️⃣ Variância e média dos 40 aprovados
- Conceito abordado: **Variância e seleção de subset de dados**.
- Método: Ordenação e seleção do top 40, seguido de `var()` e `mean()`.

### 5️⃣ Teto do terceiro quartil em Matemática e Linguagens
- Conceito abordado: **Quartis e estatística descritiva**.
- Método: Uso de `quantile(0.75)`.

### 6️⃣ & 7️⃣ Histogramas e análise de simetria
- Conceito abordado: **Distribuição de dados e visualização estatística**.
- Método: `plt.hist()` com diferentes bins e ranges para avaliar simetria.

### 8️⃣ & 9️⃣ Boxplot e remoção de outliers com IQR
- Conceito abordado: **Identificação de outliers pelo Intervalo Interquartílico (IQR)**.
- Método: Boxplot com `sns.boxplot()` e filtro via `IQR`.

### 🔟 Melhor estratégia para preencher valores nulos
- Conceito abordado: **Média vs Moda vs Mediana** como substituição.
- Método: Comparação de impacto na média e desvio padrão após imputação.

---
## 🚀 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/aflorada/python_frequencias_medidas
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o dashboard Streamlit:
   ```bash
   streamlit run app.py
   ```

---
## 📚 Referências
- Documentação oficial das bibliotecas usadas.
- Material do Bootcamp de Data Analytics.

---
## 📌 Autor
Projeto desenvolvido por **Ana Julia** como parte do **Bootcamp de Data Analytics**. 💡🚀

