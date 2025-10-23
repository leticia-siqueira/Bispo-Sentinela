import os; os.system('cls')


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
baixo e esquerda = (x - 1, y -1)


'''

# 1. Converte de Alfanumérico para Coordenada (string -> (x, y))
# !!!Lembrar que x = coluna e y = linha
def alf_to_coord(s):
    # converte a coluna
    x = ord(s[0]) - ord('a')
   
    # converte a linha
    y = int(s[1]) - 1
   
    return x, y


# 2. Coordenada para Alfanumérico (x, y) -> string
def coord_to_alf(x, y):
    # chr faz o oposto de ord
    coluna = chr(x + ord('a'))
    linha = str(y + 1)
   
    return coluna + linha


lista_posições_todos = []


bispo = input("Digite a posição do bispo: ")
lista_posições_todos.append(bispo)
bispo = alf_to_coord(bispo)


peças = set() #armazena só as coordenadas das peças inimigas, sem incluir o bispo




qtd_peças_inimigas = int(input("Digite a quantidade de peças inimigas: "))


if qtd_peças_inimigas < 0 or qtd_peças_inimigas > 63:
    while True:
        print("O número tem que ser entre 0 e 63")
        qtd_peças_inimigas = int(input("Digite uma quantidade válida: "))
        if qtd_peças_inimigas >= 0 and qtd_peças_inimigas <=63:
            break
        else:
            continue






for i in range(qtd_peças_inimigas):
    posição_inimigo = input(f"Digite a posição do inimigo {i} em notação Algébrica: ").lower()
    while True:
        if posição_inimigo in lista_posições_todos:
            print("Já tem uma peça nessa casa")
            posição_inimigo = input("Digite uma posição diferente: ")
        else:
            lista_posições_todos.append(posição_inimigo)
            peças.add(alf_to_coord(posição_inimigo))
            break


peças_capturaveis = set()


def diagonais (dx, dy,bispo,peças):
    #cima e direita = (x + 1, y + 1)
    #cima e esquerda = (x - 1, y + 1)
    #baixo e direita = (x + 1, y - 1)
    #baixo e esquerda = (x - 1, y -1)
    x,y = bispo #(2,3)


    #cálculo para qualquer diagonal:
    while x <= 7 and x >=0 or y <= 7 and y >= 0: #enquanto ele está no tabuleiro
        x += dx #dx = 1
        y += dy #dy = 1
       
       
        if (x,y) in peças:
            peças_capturaveis.add(coord_to_alf(x,y))  
            break
        else:
            continue


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
    elif i == 3: #pra cima e pra esquerda
        dx = -1
        dy = -1
        diagonais(dx,dy,bispo,peças)


if len(peças_capturaveis) == 0:
    print(0)
else:
    print(len(peças_capturaveis))
    print(sorted(peças_capturaveis))