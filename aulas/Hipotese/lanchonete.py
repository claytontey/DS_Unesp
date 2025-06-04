import numpy as np
import pandas as pd
import scipy.stats as stats

# Coletar os dados 
df = pd.read_csv("lanchonete.csv")
print(df.head())

df_tempo_entrega = pd.DataFrame(df)

# Criando nova coluna 'Tempo_entrega'
df_tempo_entrega['Tempo_Entrega'] = df_tempo_entrega['Minutos'] + (df_tempo_entrega['Segundos']/60) 
print(df_tempo_entrega.head())

# Definir a média esperada (H0: média = 30 horas)
media_esperada = 30

# Realizar o teste t para amostras únicas
t_stat, p_val = stats.ttest_1samp(df_tempo_entrega['Tempo_Entrega'], media_esperada)

# Exibir os resultados
print(f"Estatística t: {t_stat}")
print(f"p-valor: {p_val}")

# Interpretação do p-valor
alpha = 0.05
if p_val < alpha:
    print("Rejeitamos a hipótese nula (H₀). A média do valor de tempo para entrega é significativamente diferente de 30 horas.")
else:
   print("Falhamos em rejeitar a hipótese nula (H₀). A média do valor de tempo para a entrega é significativamente diferente de 30 horas.")
