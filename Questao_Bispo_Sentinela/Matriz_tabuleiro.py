''' Essa é uma parte do código para printar a matriz do tabuleiro,
ou seja, como ele ficaria montado após adicionar as peças '''


#Mostrando o tabuleiro
print("\nTabuleiro (X = bispo, 0 = peça inimiga):\n")
print("  a    b    c    d    e    f    g    h")

#cria uma matriz 8x8
matriz = []
for l in range(8):
    matriz.append([])
    for c in range(8):
        matriz[l].append(" . ")

#pega as coordenadas das peças inimigas
for (x, y) in peças:
    matriz[y][x] = " 0 " #lembrar que na hora de chamar a matriz, tem que ser (coluna x linha) e não o contrário

#pega a coordenada do bispo novamente 
bx, by = bispo
matriz[by][bx] = " X "

#Imprime de forma invertida
for l in range(7, -1, -1): #queremos que imprima da linha 7 até a 0
    for c in range(8):
        print(f"[{matriz[l][c]:^3}]", end="")
    print()