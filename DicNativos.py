import itertools

prefijo = ['004', '014', '044']
for codigo, numero in itertools.product(prefijo, range(2000000, 5000001)):
    print('{0}{1:07d}'.format(codigo, numero))

