# 1
# def z1(imie,wiek):
#     ''' Funkcja wypisuje imie oraz wiek.
#
#     :param imie:
#     :param wiek:
#     :return:
#
#     '''
#     print(imie,wiek)
# z1('Damian',19)
# z1('Bartek', 21)
# z1(wiek=23,imie="Rafał")
# print(z1.__doc__)
# print(help(z1))

# 2
# def oblicz(a,b):
#    suma = a+b
#    różnica = a-b
#    return suma , różnica
# print(oblicz(10,5))
#
# x,y=oblicz(3,2)
# print(f'suma = {x}, rożnica = {y}')

# 3
# def zad3(*args):
#     print(args)
#     for i in args:
#         print(i)
# zad3()
# zad3(1,1.5,False,[2,6])

# 3.1
def zad3(*args):
    print(args)
    for i in args:
        print(i)
zad3()
zad3(1,1.5,False,[2,6])

def max(number1,*args):
    print(*args)
    a = number1
    for z in args:
       if z>a:
           a = z
    return a
print(max(66,2,3,-5,32,44,22))
#print(max())