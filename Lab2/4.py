litera = input("podaj literę: ")
różnica = ord("a") - ord("A")

if "a" <= litera<= "z":
    print(chr(ord(litera) - różnica))
elif "A" <= litera <= "Z":
    nowa = ord(litera) + różnica
    znak = chr(nowa)
    print(znak)
else:
    print("to nie jest litera")
# ord(znak) - zwraca kod ASCII
# chr(kod) - zwraca znak
