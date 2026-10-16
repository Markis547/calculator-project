import math

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Ошибка: корень из отрицательного числа!"
    return math.sqrt(a)

def percentage(total, percent):
    return (total * percent) / 100
