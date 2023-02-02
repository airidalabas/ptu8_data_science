# Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
# Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# Įdėti sukurtus Zmogus objektus į naują sąrašą
# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)
# Patarimai:
# Naudoti sorted, attrgetter, reverse, funkciją repr
from operator import attrgetter

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f"(Vardas: {self.vardas}, Amžius: {self.amzius})")

z1 = Zmogus("Antanas", 39)
z2 = Zmogus("Žmogeliukas", 34)
z3 = Zmogus("Rokas", 24)

sarasas = [z1, z2, z3]
# print(sarasas)

def pagal_varda(obj):
    if hasattr(obj, "vardas"):
        return obj.vardas
    else:
        return str(obj)

# zmogus_vardas = sorted(sarasas, key=pagal_varda)
# print(zmogus_vardas)

zmogus_pagal_amzius = sorted(sarasas, key=lambda obj: obj.amzius, reverse=True)
print(zmogus_pagal_amzius)

#Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą bei amziu atbulai

surusiuotas = sorted(sarasas, key=attrgetter("vardas"), reverse=True)
print(surusiuotas)

surusiuotas = sorted(sarasas, key=attrgetter("amzius"), reverse=True)
print(surusiuotas)



