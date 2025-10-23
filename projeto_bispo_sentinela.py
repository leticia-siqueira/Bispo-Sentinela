import os
os.system('cls')

'''tabuleiro:
     a      b      c      d      e      f      g      h
8  (0,7)  (1,7)  (2,7)  (3,7)  (4,7)  (5,7)  (6,7)  (7,7)
7  (0,6)  (1,6)  (2,6)  (3,6)  (4,6)  (5,6)  (6,6)  (7,6)
6  (0,5)  (1,5)  (2,5)  (3,5)  (4,5)  (5,5)  (6,5)  (7,5)
5  (0,4)  (1,4)  (2,4)  (3,4)  (4,4)  (5,4)  (6,4)  (7,4)
4  (0,3)  (1,3)  (2,3)  (3,3)  (4,3)  (5,3)  (6,3)  (7,3)
3  (0,2)  (1,2)  (2,2)  (3,2)  (4,2)  (5,2)  (6,2)  (7,2)
2  (0,1)  (1,1)  (2,1)  (3,1)  (4,1)  (5,1)  (6,1)  (7,1)
1  (0,0)  (1,0)  (2,0)  (3,0)  (4,0)  (5,0)  (6,0)  (7,0)

Posição das diagonais:

cima e direita = (x + 1, y + 1)
cima e esquerda = (x - 1, y + 1)
baixo e direita = (x + 1, y - 1)
baixo e esquerda = (x - 1, y -1)]

'''

# 1. Converte de Alfanumérico para Coordenada (string -> (x, y))
# !!!Lembrar que x = coluna e y = linha 
def alf_to_coord(s):
    x = ord(s[0]) - ord('a')
    y = int(s[1]) - 1
    return x, y

def coord_to_alf(x, y):
    coluna = chr(x + ord('a'))
    linha = str(y + 1)
    return coluna + linha

#Lista criada para fazer a verificação de itens repetidos
lista_posições_todos = []

bispo = input("Digite a posição do bispo: ").lower()
lista_posições_todos.append(bispo)
bispo = alf_to_coord(bispo)

peças = set() 

qtd_peças_inimigas = int(input("Digite a quantidade de peças inimigas: "))

while qtd_peças_inimigas < 0 or qtd_peças_inimigas > 63:
    print("O número tem que ser entre 0 e 63")
    qtd_peças_inimigas = int(input("Digite uma quantidade válida: "))

for i in range(qtd_peças_inimigas):
    posição_inimigo = input(f"Digite a posição do inimigo {i+1} em notação Algébrica: ").lower()
    
    while posição_inimigo in lista_posições_todos: #verificação de itens repetidos, e se não tá ocupando aa posição do bispo
        print("Já tem uma peça nessa casa!")
        posição_inimigo = input("Digite uma posição diferente: ").lower()
    
    lista_posições_todos.append(posição_inimigo)
    peças.add(alf_to_coord(posição_inimigo))

peças_capturaveis = set()

#Função pra percorrer todas as diagonais
def diagonais(dx, dy, bispo, peças):
    #cima e direita = (x + 1, y + 1)
    #cima e esquerda = (x - 1, y + 1)
    #baixo e direita = (x + 1, y - 1)
    #baixo e esquerda = (x - 1, y -1)
    
    x, y = bispo
    while 0 <= x <= 7 and 0 <= y <= 7: #enquanto ele não saiu do tabuleiro, contudo ele ainda pode sair depois da primeira condição
        x += dx
        y += dy
        if 0 <= x <= 7 and 0 <= y <= 7:
            if (x, y) in peças:#significa que tem uma peça naquela diagonal e o bispo pode comer ele
                peças_capturaveis.add(coord_to_alf(x, y))
                break

for i in range(4):
    if i == 0: #pra cima e pra direita
        dx = 1
        dy = 1
        diagonais(dx,dy,bispo,peças)
    elif i == 1: #pra cima e pra esquerda
        dx = -1
        dy = 1
        diagonais(dx,dy,bispo,peças)
    elif i == 2: #pra baixo e direita
        dx = 1
        dy = -1
        diagonais(dx,dy,bispo,peças)
    elif i == 3: #pra baixo e pra esquerda
        dx = -1
        dy = -1
        diagonais(dx,dy,bispo,peças)


if len(peças_capturaveis) == 0:
    print("\nNenhuma peça pode ser capturada(0);-;")
else:
    print(f"\n{len(peças_capturaveis)} peça(s) podem ser capturadas:")
    print(sorted(peças_capturaveis))

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