import random

n1 = str(input("1o pessoa: "))
n2 = str(input("2o pessoa: "))
n3 = str(input("3o pessoa: "))
n4 = str(input("4o pessoa: "))
lista = [n1, n2, n3, n4]
print(f"{lista}")
random.shuffle(lista)
print(f"{lista}")
