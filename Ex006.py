nome = str(input("Escreva seu nome completo: ")).strip()
print(f"Letra maiusculas = {nome.upper()}")
print(f"Letras minusculas = {nome.lower()}")
print(len(nome.replace(" ", "")))
print(len(nome.split()[0]))