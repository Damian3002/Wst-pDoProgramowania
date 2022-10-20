a = (int)(input("Proszę podać wiek klienta: "))
if a<4:
    print("Wstęp jest bezpłatny")
elif a<=18:
    print("Cena biletu: 10zł")
else:
    print("Cena biletu kosztuje 20zł")