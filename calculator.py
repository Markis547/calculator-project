
import math

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Ошибка: корень из отрицательного числа!"
    return math.sqrt(a)

def percentage(total, percent):
    return (total * percent) / 100

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

