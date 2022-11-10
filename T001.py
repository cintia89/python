i = '\033[m'
a = '\033[34m'
v = '\033[31m'
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
if n1 > n2:
    print(f"{a}SIM{i}")
else:
    print(f"{v}NÃO{i}")
