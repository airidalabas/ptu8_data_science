# skaiciai = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
# def generatorius(skaiciai):
#     for skaicius in skaiciai:
#         yield skaicius
# for skaicius in generatorius(skaiciai):
#     print(skaicius) #spausdina viska iskart

#spausdinti po viena:
# x = generatorius(skaiciai)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# spausdinti = fibonacci()
# print(next(spausdinti))
# print(next(spausdinti))
# print(next(spausdinti))
# # for a in fibonacci():
# #     print(a) pasileidzia begalinis ciklas

    pirmesnis_sk, sekantis_sk = 0, 1 
    while True:
        yield pirmesnis_sk # kai yield eina pries israiska prasideda nuo pradzios
        pirmesnis_sk, sekantis_sk = pirmesnis_sk + sekantis_sk, pirmesnis_sk
        #yield pirmesnis_sk #kai yield eina po israiska viena reiksme prasoka
        

spausdinti = fibonacci()
print(next(spausdinti))
print(next(spausdinti))
print(next(spausdinti))
print(next(spausdinti))





        

