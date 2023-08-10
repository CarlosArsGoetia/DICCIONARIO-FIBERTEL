import itertools


prefijo = ['004', '014', '044']
for codigo, numero in itertools.product(prefijo, range(9000000, 9999999)):
    print('{0}{1:07d}'.format(codigo, numero))

    
