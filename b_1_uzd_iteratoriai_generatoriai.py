#skaiciai = range(0, 50)
def saraso_skaiciai(skaiciai):
    for skaicius in skaiciai:
        yield skaicius +2
        #skaicius +=2
poriniai = saraso_skaiciai(range(0, 50, 2))
print(next(poriniai))
print(next(poriniai))
print(next(poriniai))


# def poriniai():
#     number = 2
#     while True:
#         yield number
#         number += 2
# skaiciuoti = poriniai()
# print(next(skaiciuoti))
# print(next(skaiciuoti))
# print(next(skaiciuoti))
# print(next(skaiciuoti))
 
# num = 0
# g = (num for num in range(2, 50, 2))
# print(next(g))
# print(next(g))
# print(next(g))




    