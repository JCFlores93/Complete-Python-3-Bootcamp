# def myfunc(value: bool):
#     if value: 
#         return 'Hello'
#     else:
#         return 'Goodbye'

# def myfunc(x, y, z):
#     if z: 
#         return x
#     else:
#         return y

# def myfunc(x, y):
#     return x + y
def is_even(x):
    return x % 2 == 0

def is_greater(x, y):
    return x > y

# def myfunc(*args):
#     return [ x for x in args if x % 2 == 0]

# even par -> upperacase
# odd impar -> lowecase
def myfunc(word):
    s: string = ''
    for i in range(len(word)):
        if i % 2 == 0:
            s = s + word[i].upper()
        else:
            s = s + word[i].lower()
    return s
myfunc('hola')
