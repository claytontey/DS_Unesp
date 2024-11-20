import streamlit as st
import pandas as pd
import plotly.express as px

# Título principal
st.title("Dashboard Interativo: Análise do Conjunto de Dados Iris")
st.markdown("""
Este dashboard permite a exploração interativa do famoso conjunto de dados **Iris**, utilizado amplamente em análises de ciência de dados. 
Você pode filtrar por espécie e visualizar gráficos interativos com base nas características da planta.
""")

# Carregar o dataset Iris
df = px.data.iris()

# Barra lateral para navegação
st.sidebar.title("Navegação")
section = st.sidebar.radio("Escolha a seção", ["Visão Geral", "Gráficos Interativos", "Estatísticas Descritivas"])

# Filtro interativo: escolha da espécie
species = st.sidebar.selectbox('Escolha a espécie para visualização', df['species'].unique())

# Filtrar o dataset com base na espécie selecionada
filtered_df = df[df['species'] == species]

# Seção: Visão Geral
if section == "Visão Geral":
    st.subheader("Visão Geral do Conjunto de Dados Iris")
    st.write(f"Exibindo as primeiras 10 amostras da espécie selecionada: **{species}**")
    st.write(filtered_df.head(10))

    st.markdown(f"""
    - **Número de amostras na espécie {species}**: {len(filtered_df)}
    - **Variáveis disponíveis**: Comprimento e largura da sépala e da pétala.
    """)

# Seção: Gráficos Interativos
elif section == "Gráficos Interativos":
    st.subheader(f"Gráficos Interativos para a Espécie: {species}")

    # Gráfico de Dispersão: Sepal Width vs. Sepal Length
    st.markdown("### Gráfico de Dispersão: Sepal Width vs. Sepal Length")
    fig1 = px.scatter(filtered_df, x='sepal_width', y='sepal_length', color='species', title=f"Dispersão da Sépala para {species}")
    st.plotly_chart(fig1)

    # Gráfico de Histograma: Petal Length
    st.markdown("### Histograma do Comprimento da Pétala")
    fig2 = px.histogram(filtered_df, x='petal_length', nbins=20, title=f"Distribuição do comprimento da pétala para {species}")
    st.plotly_chart(fig2)

# Seção: Estatísticas Descritivas
elif section == "Estatísticas Descritivas":
    st.subheader(f"Estatísticas Descritivas da Espécie: {species}")
    st.write(filtered_df.describe())

    # Layout em colunas para exibir diferentes estatísticas lado a lado
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Estatísticas da Sépala")
        fig3 = px.box(filtered_df, y="sepal_length", title="Distribuição do Comprimento da Sépala")
        st.plotly_chart(fig3)

    with col2:
        st.markdown("#### Estatísticas da Pétala")
        fig4 = px.box(filtered_df, y="petal_length", title="Distribuição do Comprimento da Pétala")
        st.plotly_chart(fig4)

# Mostrar métricas
st.sidebar.markdown("### Métricas da Espécie")
st.sidebar.metric(label="Média do Comprimento da Sépala", value=f"{filtered_df['sepal_length'].mean():.2f}")
st.sidebar.metric(label="Média do Comprimento da Pétala", value=f"{filtered_df['petal_length'].mean():.2f}")

# Finalizando com observações
st.sidebar.markdown("""
- **Espécies disponíveis**: Setosa, Versicolor, Virginica.
- A navegação acima permite comparar e explorar diferentes espécies de maneira interativa.
""")
