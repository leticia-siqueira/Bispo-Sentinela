# Bispo-Sentinela
Esse é um código que estimula a lógica de programação e ajuda a fixar os conhecimentos sobre a linguagem Python

## O desafio
Dado um tabuleiro de xadrez 8×8, a posição de um bispo e as posições de n peças inimigas,
determine quais peças podem ser capturadas pelo bispo em um único lance. O bispo move-se
em diagonais e não pula casas. Em cada uma das quatro diagonais que partem do bispo,
apenas a primeira peça (a mais próxima), se houver, pode ser capturada; qualquer peça atrás
dela na mesma diagonal não pode ser capturada.

## Entrada
● Uma linha com a posição do bispo em notação algébrica (a1 a h8).\
● Uma linha com o inteiro n (0 ≤ n ≤ 63), o número de peças inimigas.\
● n linhas seguintes, cada uma com a posição de uma peça inimiga em notação
algébrica.

## Restrições e Assunções
● Não há peças aliadas além do próprio bispo. \
● Nenhuma peça inimiga ocupa a mesma casa do bispo e não há posições duplicadas.\
● Notação válida: colunas a...h, linhas 1...8 (ex.: d5).

## Saída
● Primeira linha: um inteiro k, a quantidade de peças que o bispo pode capturar em um
único lance.\
● Segunda linha (apenas se k > 0): as k posições capturáveis, ordenadas
lexicograficamente (por coluna e depois por linha), separadas por espaço.\
● Se k = 0, imprima apenas 0 na primeira linha.
