"""6. Описати функцію ArcСos1(X) дійсного типу(X - дійсне , задано в градусах). Скласти
програму розв’язку рівняння cos(аx+b)=c. """

from math import cos
from random import uniform

x = float(input("x: "))
a = float(input("a: "))
b = float(input("b: "))
def ArcCos1(x):

    y = cos(a * x + b)


    return y

print("sin(ax + b) =", ArcCos1(x))


