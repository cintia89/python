import math
N = float(input("Digite um numero: "))
raiz = math.sqrt(N)
print("A raiz de {} vale {}".format(N, raiz))
arrendo = math.ceil(raiz)
print("O arredondamento dessa raiz vale {}".format(arrendo))
