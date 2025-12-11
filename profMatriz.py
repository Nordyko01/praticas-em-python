linhas = int(input("Digite número de linhas: "))
colunas =  int(input("Digite número de linhas: "))


matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"digite o valor[{i}{j}]: "))
        linha.append(valor)
    matriz.append(linha)
    print("Matriz", matriz)