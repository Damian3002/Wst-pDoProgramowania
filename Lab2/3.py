print(''' Jaką operację chcesz wykonać? 1) dodawanie 2) odejmowanie 3) mnożenie 4) dzielenie 5) potęgowanie ''')
opcja=int(input("Podaj operację: "))
a=int(input("Podaj argument 1: "))
b=int(input("Podaj argument 2: "))
if opcja == 1:
    wynik= a+b
elif opcja == 2:
    wynik= a-b
elif opcja == 3:
    wynik= a*b
elif opcja == 4:
    if b == 0:
        print("Nie dziel przez 0")
        exit()
    wynik = a / b
elif opcja == 5:
    wynik= a**b
else:
    print("niepoprawna operacja")
    exit()
print("Wynik", wynik)