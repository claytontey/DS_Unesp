import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# Coletar os dados (exemplo fictício com 13 funcionários e a quantidade de horas trabalhadas por semana)
horas_trabalhadas = [38, 42, 45, 39, 41, 40, 44, 43, 39, 40, 42, 38, 37]

# Definir a média esperada (H0: média = 40 horas)
media_esperada = 40

# Realizar o teste t para amostras únicas
t_stat, p_val = stats.ttest_1samp(horas_trabalhadas, media_esperada)

# Exibir os resultados
print(f"Estatística t: {t_stat}")
print(f"p-valor: {p_val}")

# Interpretação do p-valor
alpha = 0.05
if p_val < alpha:
    print("Rejeitamos a hipótese nula (H₀). A média das horas trabalhadas é significativamente diferente de 40 horas.")
else:
    print("Falhamos em rejeitar a hipótese nula (H₀). A média das horas trabalhadas não é significativamente diferente de 40 horas.")
