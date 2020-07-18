import sys


argumentos = len(sys.argv)
if argumentos != 2:
    print('Solo se admite una cadena de texto')
else:
    print('{}'.format(str(sys.argv[1]).swapcase()))
