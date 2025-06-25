import random

# Lista de alunos
alunos = [
    "Alberto Azevedo Martinez", "Arthur Serafim Gomes Inacio", "Caio Ribeiro de Carvalho",
    "Darryê Roberto da Silva Mellin", "Eduardo Conde Pires", "Gabriel Augusto Moreli",
    "Gabriel de Mello Cruz", "Guilherme Lima Zanin", "Guilherme Mendonça Pinheiro",
    "Guilherme Montes de Luca", "Guilherme Pandolfi da Silva", "João Lucas Cardoso Criveli",
    "Leonardo Vieira Maurino", "Lucas Mendes Mussato Fernandes", "Luciano Henrique Arendt Rodrigues",
    "Marco Antônio Cerqueira de Queiroz", "Maria Alice Gonçalves", "Rafaela Issa Tonon",
    "Sofia Azevedo Rosa", "Thiago Henrique Moço Fonseca", "Vinícius Casimiro da Silveira",
    "Vitor Siwerski Aronque"
]

# Lista de temas
temas = [
    "Sono x Produtividade",
    "Tempo de Estudo x Notas",
    "Redes Sociais x Ansiedade",
    "Estresse x Alimentação",
    "Atividade Física x Qualidade do Sono",
    "Música x Raciocínio",
    "Treinos x Autoestima",
    "Cafeína x Produtividade",
    "Animais x Produção (Agro)",
    "Lazer x Felicidade"
]

# Embaralhar as listas para sortear aleatoriamente
random.shuffle(alunos)
random.shuffle(temas)

# Atribuir temas (com repetição se necessário)
sorteio = {aluno: temas[i % len(temas)] for i, aluno in enumerate(alunos)}

# Exibir resultados
print("🎲 Sorteio de Temas para os Alunos:\n")
for aluno, tema in sorteio.items():
    print(f"{aluno} → {tema}")
