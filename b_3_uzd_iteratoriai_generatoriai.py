# from random import randint
# pin = "0549"
# def skaiciai(): 
#     skaicius = 0 
#     while skaicius < 10000:
#         
# def my_range(n):
#     print("pradzia")
#     pradzia=1
#     while pradzia < n:
#         print("my_range apduoda po skaiciu")
#         yield pradzia
#         pradzia +=1
# big_range = my_range(5)
# print(next(big_range))
# print(next(big_range))


# print("kas liko sarase:")
# print(list(big_range))

# for pradzia in my_range(6):
#     print(pradzia) #spausdina viska iskart

# a = 2
# b = 3
# print(f"a is {a}, b is {b}")
# # a, b = b, a
# #arba 
# c = a
# a = b
# b = c
# print(f"a is {a}, b is {b}")

def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2
# go_range = oddnumbers()
# print(next(go_range))
# print(next(go_range))
# print(next(go_range))
# print(next(go_range))

def pi_series():
    odds = oddnumbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation

approx_pi = pi_series()
for x in range(10):
    print(next(approx_pi))
