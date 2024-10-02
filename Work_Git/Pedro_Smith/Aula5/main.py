import numpy as np

a = [2,4,6,8,10]
b = [1,3,5,7,9]
c = []

c = [(a[i] * 2) + (b[i] * 3) for i in range(len(a))]

print(c)

#for i in range(len(a)):
#    a[i] = i ** 2
#    b[i] = i ** 3
#    c.append(a[i] + b[i])

#c = a + b

#print(a,b,c)

# List comprenhension
    # operação  #count  #intervalo
a = [i ** 2 for i in range(len(a))]
b = [i ** 3 for i in range(len(b))]
c = [a[i] + b[i] for i in range(len(a))]

print(a,b,c)

c = [i ** 2 + i ** 3 for i in range(len(a))]

print(c)

acessorios_exerc1 = [
    'Rodas de liga',
    'Travas elétricas',
    'Piloto automatico',
    'Bancos de couro',
    'Ar condicionado'
]

acessorios_exerc1.insert(0, acessorios_exerc1.pop(-1))
acessorios_exerc1.insert(0,'Airbag')

print(acessorios_exerc1)