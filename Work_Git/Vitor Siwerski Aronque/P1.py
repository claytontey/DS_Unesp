import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#lendo csv do caminho relativo
df = pd.read_csv("Work_Git\Vitor Siwerski Aronque\cafe_produtividade.csv")

#renomeando as colunas
df.columns = [
    "timestamp", "consome_cafe", "xic_por_dia", "horario_cafe", "periodo_produtivo","atribui_ao_cafe", "prod_sem_cafe", "prod_com_cafe", "horas_sono", "outros_estimulantes"
]

#transformacao dos dados
df["xic_por_dia"] = df["xic_por_dia"].replace("Nenhuma", 0).replace("4 ou mais", 4).astype(int)
df["atribui_ao_cafe"] = df["atribui_ao_cafe"].replace(1, "Discordo completamente").replace(2, "Discordo um pouco").replace(3, "Neutro").replace(4, "Concordo um pouco").replace(5, "Concordo completamente").astype(str)
df["prod_sem_cafe"] = pd.to_numeric(df["prod_sem_cafe"], errors="coerce")
df["prod_com_cafe"] = pd.to_numeric(df["prod_com_cafe"], errors="coerce")

###########################################################################

def tabela_frequencia(col, nome):
    print(f"{nome}")
    f_absoluta = col.value_counts()
    f_relativa = col.value_counts(normalize=True).round(2)
    f_absoluta_acumulada = f_absoluta.cumsum()
    f_relativa_acumulada = f_relativa.cumsum()
    tabela = pd.DataFrame({
        "Frequencia Absoluta": f_absoluta,
        "Frequencia Relativa": f_relativa * 100,
        "Frequencia Acumulada": f_absoluta_acumulada,
        "Frequencia Relativa Acumulada": f_relativa_acumulada * 100
    })
    print(tabela) 
    print("\n\n")


tabela_frequencia(df["consome_cafe"], "Consome café")
tabela_frequencia(df["horas_sono"], "Horas de sono por noite")
tabela_frequencia(df["atribui_ao_cafe"], "Atribui produtividade ao café")

###########################################################################

def estatisticas(col, nome):
    print(f"{nome}")
    print(f"Media: {col.mean():.2f}")
    print(f"Moda: {col.mode().values}")
    print(f"Mediana: {col.median():.2f}") 
    print("\n\n")

estatisticas(df["xic_por_dia"], "Xícaras de café por dia")
estatisticas(df["prod_com_cafe"], "Produtividade com café")

###########################################################################

sns.set_theme(style="whitegrid")

#grafico de barras - consumo de cafe
plt.figure(figsize=(6, 4))
sns.countplot(x="consome_cafe", data=df)
plt.title("Consumo de Café")
plt.ylabel("Frequência")
plt.xlabel("Consome café?")
plt.show()

#histograma - produtividade com cafe
plt.figure(figsize=(6, 4))
sns.histplot(df["prod_com_cafe"], bins=10, kde=True, color="green")
plt.title("Produtividade com Café")
plt.xlabel("Produtividade (0 a 10)")
plt.ylabel("Frequência")
plt.show()