n = int(input('Digite n: '))

n1, n2 = 0, 1
aux = 0

if n <= 0:
    print('Sólo enteros positivos')
elif 0 < n <= 2:
    print(n1, n2, end=' ')
else:
    print(n1, n2, end=' ')
    for x in range(2, n):
        n3 = n1 + n2
        if n3 % 2 != 0:
            print(n3, end=' ')
        n1 = n2
        n2 = n3
