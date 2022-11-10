import random

inicio = int(input("Inicio = "))
fim = int(input("Fim = "))
computador = random.randint(inicio, fim)

print("O computador escolher {}".format(computador))
