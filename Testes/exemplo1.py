import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import ttest_ind, levene, shapiro
import warnings
warnings.filterwarnings('ignore')

# Configuração para gráficos
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# ========================================
# 1. GERAÇÃO DE DADOS SIMULADOS
# ========================================

np.random.seed(42)

# Dados do grupo controle (método tradicional)
n_controle = 50
vendas_controle = np.random.normal(loc=15000, scale=3000, size=n_controle)
vendas_controle = np.clip(vendas_controle, 5000, None)  # Vendas mínimas de 5k

# Dados do grupo experimental (novo método)
n_experimental = 48
vendas_experimental = np.random.normal(loc=17500, scale=3200, size=n_experimental)
vendas_experimental = np.clip(vendas_experimental, 5000, None)

# Criando DataFrame
dados = pd.DataFrame({
    'vendas': np.concatenate([vendas_controle, vendas_experimental]),
    'grupo': ['Controle'] * n_controle + ['Experimental'] * n_experimental,
    'vendedor_id': range(1, n_controle + n_experimental + 1)
})

print("="*60)
print("ANÁLISE DE DADOS: TESTE DE HIPÓTESE")
print("Impacto do Novo Método de Treinamento nas Vendas")
print("="*60)

# ========================================
# 2. ANÁLISE EXPLORATÓRIA
# ========================================

print("\n📊 ESTATÍSTICAS DESCRITIVAS")
print("-"*40)
resumo = dados.groupby('grupo')['vendas'].agg([
    'count', 'mean', 'median', 'std', 'min', 'max'
]).round(2)
resumo.columns = ['N', 'Média', 'Mediana', 'Desvio Padrão', 'Mínimo', 'Máximo']
print(resumo)

# Diferença entre médias
diff_medias = dados[dados['grupo'] == 'Experimental']['vendas'].mean() - \
              dados[dados['grupo'] == 'Controle']['vendas'].mean()
print(f"\n💡 Diferença entre médias: R$ {diff_medias:,.2f}")

# ========================================
# 3. VISUALIZAÇÕES
# ========================================

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Análise Comparativa: Vendas por Grupo', fontsize=16, fontweight='bold')

# Boxplot
sns.boxplot(data=dados, x='grupo', y='vendas', ax=axes[0,0])
axes[0,0].set_title('Distribuição das Vendas por Grupo')
axes[0,0].set_ylabel('Vendas (R$)')
axes[0,0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R${x/1000:.0f}k'))

# Histograma
for grupo, cor in zip(['Controle', 'Experimental'], ['skyblue', 'lightcoral']):
    dados_grupo = dados[dados['grupo'] == grupo]['vendas']
    axes[0,1].hist(dados_grupo, alpha=0.7, label=grupo, bins=15, color=cor, edgecolor='black')
axes[0,1].set_title('Distribuição das Vendas')
axes[0,1].set_xlabel('Vendas (R$)')
axes[0,1].set_ylabel('Frequência')
axes[0,1].legend()
axes[0,1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}k'))

# Q-Q Plot para normalidade
from scipy.stats import probplot
probplot(dados[dados['grupo'] == 'Controle']['vendas'], dist="norm", plot=axes[1,0])
axes[1,0].set_title('Q-Q Plot - Grupo Controle')
axes[1,0].grid(True)

probplot(dados[dados['grupo'] == 'Experimental']['vendas'], dist="norm", plot=axes[1,1])
axes[1,1].set_title('Q-Q Plot - Grupo Experimental')
axes[1,1].grid(True)

plt.tight_layout()
plt.show()

# ========================================
# 4. FORMULAÇÃO DAS HIPÓTESES
# ========================================

print("\n🎯 FORMULAÇÃO DAS HIPÓTESES")
print("-"*40)
print("H₀ (Hipótese Nula): μ_experimental = μ_controle")
print("    O novo método NÃO melhora o desempenho de vendas")
print("\nH₁ (Hipótese Alternativa): μ_experimental > μ_controle")
print("    O novo método MELHORA o desempenho de vendas")
print("\nNível de significância (α): 0.05")
print("Teste: Unilateral à direita (one-tailed)")

# ========================================
# 5. VERIFICAÇÃO DE PRESSUPOSTOS
# ========================================

print("\n🔍 VERIFICAÇÃO DE PRESSUPOSTOS")
print("-"*40)

# Teste de normalidade (Shapiro-Wilk)
_, p_norm_controle = shapiro(dados[dados['grupo'] == 'Controle']['vendas'])
_, p_norm_experimental = shapiro(dados[dados['grupo'] == 'Experimental']['vendas'])

print("1. Normalidade (Shapiro-Wilk):")
print(f"   Controle: p-valor = {p_norm_controle:.4f}")
print(f"   Experimental: p-valor = {p_norm_experimental:.4f}")

if p_norm_controle > 0.05 and p_norm_experimental > 0.05:
    print("   ✅ Ambos os grupos seguem distribuição normal")
    normalidade_ok = True
else:
    print("   ⚠️  Pelo menos um grupo não segue distribuição normal")
    normalidade_ok = False

# Teste de homogeneidade das variâncias (Levene)
_, p_levene = levene(dados[dados['grupo'] == 'Controle']['vendas'],
                     dados[dados['grupo'] == 'Experimental']['vendas'])

print(f"\n2. Homogeneidade das variâncias (Levene): p-valor = {p_levene:.4f}")
if p_levene > 0.05:
    print("   ✅ Variâncias homogêneas")
    var_igual = True
else:
    print("   ⚠️  Variâncias diferentes")
    var_igual = False

# ========================================
# 6. TESTE DE HIPÓTESE
# ========================================

print("\n🧪 TESTE DE HIPÓTESE")
print("-"*40)

# Separando os dados
vendas_controle = dados[dados['grupo'] == 'Controle']['vendas']
vendas_experimental = dados[dados['grupo'] == 'Experimental']['vendas']

# Escolhendo o teste apropriado
if normalidade_ok and var_igual:
    # Teste t de Student para amostras independentes
    estatistica, p_valor = ttest_ind(vendas_experimental, vendas_controle, 
                                    equal_var=True, alternative='greater')
    teste_usado = "Teste t de Student (variâncias iguais)"
elif normalidade_ok and not var_igual:
    # Teste t de Welch
    estatistica, p_valor = ttest_ind(vendas_experimental, vendas_controle, 
                                    equal_var=False, alternative='greater')
    teste_usado = "Teste t de Welch (variâncias diferentes)"
else:
    # Teste de Mann-Whitney (não paramétrico)
    from scipy.stats import mannwhitneyu
    estatistica, p_valor = mannwhitneyu(vendas_experimental, vendas_controle, 
                                       alternative='greater')
    teste_usado = "Teste de Mann-Whitney (não paramétrico)"

print(f"Teste utilizado: {teste_usado}")
print(f"Estatística do teste: {estatistica:.4f}")
print(f"P-valor: {p_valor:.4f}")

# ========================================
# 7. DECISÃO E INTERPRETAÇÃO
# ========================================

print("\n📊 RESULTADOS DO TESTE")
print("-"*40)

alpha = 0.05
if p_valor < alpha:
    decisao = "REJEITAR H₀"
    conclusao = "ACEITAR H₁"
    interpretacao = "Há evidências estatísticas de que o novo método melhora o desempenho de vendas"
    significativo = "✅ ESTATISTICAMENTE SIGNIFICATIVO"
else:
    decisao = "FALHAR EM REJEITAR H₀"
    conclusao = "NÃO ACEITAR H₁"
    interpretacao = "Não há evidências suficientes para afirmar que o novo método melhora o desempenho"
    significativo = "❌ NÃO ESTATISTICAMENTE SIGNIFICATIVO"

print(f"Decisão: {decisao}")
print(f"Conclusão: {conclusao}")
print(f"Resultado: {significativo}")
print(f"\nInterpretação: {interpretacao}")

# ========================================
# 8. ANÁLISE DO TAMANHO DO EFEITO
# ========================================

print("\n📏 ANÁLISE DO TAMANHO DO EFEITO")
print("-"*40)

# Cohen's d
media_exp = vendas_experimental.mean()
media_ctrl = vendas_controle.mean()
dp_pooled = np.sqrt(((len(vendas_experimental)-1)*vendas_experimental.var() + 
                     (len(vendas_controle)-1)*vendas_controle.var()) / 
                    (len(vendas_experimental) + len(vendas_controle) - 2))

cohens_d = (media_exp - media_ctrl) / dp_pooled

print(f"Cohen's d: {cohens_d:.3f}")

if abs(cohens_d) < 0.2:
    tamanho_efeito = "Pequeno"
elif abs(cohens_d) < 0.5:
    tamanho_efeito = "Pequeno a Médio"
elif abs(cohens_d) < 0.8:
    tamanho_efeito = "Médio a Grande"
else:
    tamanho_efeito = "Grande"

print(f"Interpretação: Efeito {tamanho_efeito}")

# Percentual de melhoria
perc_melhoria = ((media_exp - media_ctrl) / media_ctrl) * 100
print(f"Melhoria percentual: {perc_melhoria:.1f}%")

# ========================================
# 9. ANÁLISE CRÍTICA DOS RESULTADOS
# ========================================

print("\n🔍 ANÁLISE CRÍTICA DOS RESULTADOS")
print("-"*40)

print("1. SIGNIFICÂNCIA ESTATÍSTICA vs PRÁTICA:")
print(f"   • Diferença média: R$ {diff_medias:,.2f}")
print(f"   • Melhoria relativa: {perc_melhoria:.1f}%")
print(f"   • Tamanho do efeito: {tamanho_efeito}")

print("\n2. LIMITAÇÕES DO ESTUDO:")
print("   • Dados simulados - resultados podem não refletir realidade")
print("   • Outras variáveis não controladas (experiência, setor, etc.)")
print("   • Período de observação não especificado")
print("   • Custo-benefício do novo método não avaliado")

print("\n3. RECOMENDAÇÕES:")
if p_valor < alpha:
    print("   • Implementar o novo método em escala piloto")
    print("   • Monitorar resultados por período mais longo")
    print("   • Analisar custo-benefício da implementação")
    print("   • Considerar fatores qualitativos (satisfação, tempo)")
else:
    print("   • Não implementar o novo método baseado nestes dados")
    print("   • Investigar outras estratégias de melhoria")
    print("   • Aumentar tamanho da amostra se possível")
    print("   • Analisar subgrupos específicos")

print("\n4. CONFIANÇA NO RESULTADO:")
intervalo_confianca = stats.t.interval(0.95, 
                                      len(vendas_experimental)-1,
                                      loc=media_exp,
                                      scale=stats.sem(vendas_experimental))
print(f"   • IC 95% para média experimental: R$ {intervalo_confianca[0]:,.0f} - R$ {intervalo_confianca[1]:,.0f}")

# ========================================
# 10. VISUALIZAÇÃO FINAL
# ========================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico de barras com intervalo de confiança
medias = [vendas_controle.mean(), vendas_experimental.mean()]
erros = [stats.sem(vendas_controle), stats.sem(vendas_experimental)]
grupos = ['Controle', 'Experimental']
cores = ['lightblue', 'lightcoral']

bars = ax1.bar(grupos, medias, yerr=erros, capsize=10, color=cores, 
               edgecolor='black', alpha=0.8)
ax1.set_title('Comparação das Médias de Vendas\n(com Erro Padrão)')
ax1.set_ylabel('Vendas Médias (R$)')
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R${x/1000:.0f}k'))

# Adicionando valores nas barras
for bar, media in zip(bars, medias):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
             f'R${media:,.0f}', ha='center', va='bottom', fontweight='bold')

# Violin plot
sns.violinplot(data=dados, x='grupo', y='vendas', ax=ax2, palette=['lightblue', 'lightcoral'])
ax2.set_title('Distribuição Completa das Vendas')
ax2.set_ylabel('Vendas (R$)')
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R${x/1000:.0f}k'))

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("RESUMO EXECUTIVO")
print("="*60)
print(f"Teste Realizado: {teste_usado}")
print(f"P-valor: {p_valor:.4f} | Alpha: {alpha}")
print(f"Resultado: {significativo}")
print(f"Diferença média: R$ {diff_medias:,.2f} ({perc_melhoria:.1f}%)")
print(f"Tamanho do efeito: {tamanho_efeito} (Cohen's d = {cohens_d:.3f})")
print("="*60)