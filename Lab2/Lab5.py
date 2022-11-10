# 2

# import random
# zestaw_1 = []
# n = int(input("podaj rozmiar listy: "))
# for i in range(n):
#     x = random.randint(1, 10)
#     zestaw_1.append(x)
# print(zestaw_1)
# n = int(input("podaj rozmiar listy: "))
# zestaw_2 = [random.randint(5, 15) for i in range(n)]
# print(zestaw_2)
#
# liczba = int(input("podaj liczbę: "))
# if liczba in zestaw_1:
#     print("liczna z zestawu pierwszego: ")
# elif liczba in zestaw_2:
#     print("liczna z zestawu drugiego: ")
# else:
#     print("liczba nie występuje w żadnym z zestawów")
#
#
# zestaw_1_2 = zestaw_1 + zestaw_2
# zestaw_1_2.sort()
# print("zestaw_1_2: " , zestaw_1_2)

# 3
# zwierzęta = []
# for i in range(4):
#     x = input("Napisz nazwy zwierzat do listy: ")
#     zwierzęta.append(x)
# zwierzęta.sort()
# print(zwierzęta[0] , zwierzęta[-3: ] , len(zwierzęta))

# 5
# import random
# punkty = []
# ponizej = []
#
# for x in range(15):
#     punkty.append(round(random.uniform(0 ,50),2))
#
# print(punkty)
# print(f" wartosc minimalna: {min(punkty)}")
# print(f" wartosc maksymalna: {max(punkty)}")
#
# liczba = float(input("podaj liczbe: "))
# if liczba in punkty:
#     print(punkty.index(liczba))
# else:
#     print("nie ma takiej liczby")
# suma = sum(punkty)
# srednia=suma/15
# print(f"srednia ilosc punktow: {srednia}")
#
# for y in punkty:
#     if y < srednia:
#         ponizej.append(y)
# powyzej = [y for y in punkty if y> srednia]
# print(f"osoby ponizej sredniej {ponizej} , osoby powyzej sredniej {powyzej}")
# print(len(ponizej), len(powyzej))

# 6
# x = list(range(10))
# print(x)
# x[:0]=x[-3:]
# print(x)
# #del x[-3:]
# x[-3:]=[]
# print(x)
#
# y=x[:]
# y[4]=100
# print(x)
# print(y)