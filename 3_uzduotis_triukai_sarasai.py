# ; Duotas sąrašas: sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# ; Sukurti programą, kuri:

# ; Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
# ; Sudėtų ir atspausdintų visus sąrašo žodžius
# ; Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme
# ; Patarimai:

# ; Naudoti filter arba comprehension, sum, " ".join() = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

suma = sum(filter(lambda x: type(x) is int or type(x) is float, sarasas))
print(suma)

stringai = sum(x for x in sarasas if type(x) is int or type(x) is float)
print(stringai)

skaiciai = sum(type(skaicius) is int for skaicius in sarasas)
print(skaiciai)

zodziai = filter(lambda zodis: type(zodis) is str, sarasas)
print(" ".join(zodziai))

zodziai = [zodis for zodis in  sarasas if type(zodis) is str]
print(" ".join(zodziai))

tiesa = sum(x for x in sarasas if x == True)
print(tiesa)

tiesa = filter(lambda x: x == True, sarasas)
print(sum(tiesa))

rezultatas = len(list(filter(lambda x: x == True, sarasas)))
print(rezultatas)

zodziai = sum(type(zodis) is str for zodis in sarasas)
print(zodziai)

