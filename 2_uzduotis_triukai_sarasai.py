from statistics import mean, median, mode
# Sukurti programą, kuri:

# Sukurtų sąrašą iš skaičių nuo 0 iki 50
# Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
# Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
# Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų. Šį sąrašą (list masyvą) priskirti naujam kintamajam.
# Su kvadratų sąrašu (nauju kintamuoju) atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
# Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
# Patarimai:
# Naudoti map, filter arba comprehension, sum, min, max, mean, median, %

sarasas = list(range(0, 50))
# daugyba_10 = map(lambda skaicius: skaicius * 10, sarasas)
# print(list(daugyba_10))

# dalyba_7 = filter(lambda skaicius: skaicius % 7 == 0, sarasas)
# print(list(dalyba_7))

kvadratu = map(lambda skaicius: skaicius **2, sarasas)
kvadratu_sarasas=(list(kvadratu))
# print(kvadratu_sarasas)

# suma = sum(kvadratu_sarasas)
# print(suma)

minimalus = min(kvadratu_sarasas)
print(minimalus)

maksimalus = max(kvadratu_sarasas)
print(maksimalus)

vidurkis = mean(kvadratu_sarasas)
print(vidurkis)

vidurinis = median(kvadratu_sarasas)
print(vidurinis)

print(mode(kvadratu_sarasas))

surusiuotas = sorted(kvadratu_sarasas)
apverstas = surusiuotas.reverse()
print(surusiuotas)


