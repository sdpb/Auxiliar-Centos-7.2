from numpy import sum as sum_np
from numpy import prod as prod_np
from numpy import trace, fliplr
from numpy.random import random


def sumatoria_columnas(matriz):
    return 'Sumatoria Columnas: {}'.format(sum_np(matriz, axis=0))


def sumatoria_filas(matriz):
    return 'Sumatoria Filas: {}'.format(sum_np(matriz, axis=1))


def sumatoria_matriz(matriz):
    return 'Sumatoria elementos: {}'.format(sum_np(matriz))


def productoria_matriz(matriz):
    matriz[matriz % 2 == 0] = 1
    return 'Productoria impares: {}'.format(prod_np(matriz))


def resta_diagonales(matriz):
    principal = trace(matriz)
    secundaria = trace(fliplr(matriz))

    return 'Resta diagonales {}'.format(principal - secundaria)


def generar_matriz(filas, columnas):
    matriz = random((filas, columnas)) * 50
    matriz = matriz.astype(int)
    return matriz


if __name__ == "__main__":
    m = int(input('Ingresar número de filas: '))
    n = int(input('Ingresar número de columnas: '))

    mtz = generar_matriz(m, n)
    print('\n {} \n'.format(mtz))

    print('1.1) {}'.format(sumatoria_filas(mtz)))
    print('1.2) {}'.format(sumatoria_columnas(mtz)))
    print('2) {}'.format(sumatoria_matriz(mtz)))
    print('3) {}'.format(resta_diagonales(mtz)))
    print('4) {}'.format(productoria_matriz(mtz)))
