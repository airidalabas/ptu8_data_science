from functools import wraps
def only_string(fun):
    @wraps(fun)
    def wrapper(text):
        if type(text) != str:
            return "Must be string."
        else:
            result = fun(text)
            return result
    return wrapper

@only_string
def your_text(text):
    return text
print(your_text())

# @only_string
# def your_text(text):
#     new = text
#     return new
# text = input("ivesti teskata:")
# print(your_text(text)) #neveikia taip kaip turi veikti







