""" Описати функцію SumRange (A, B) цілого типу, яка знаходить суму всіх цілих
чисел від A до B включно (A і B - цілі). Якщо A> B, то функція повертає 0. За
допомогою цієї функції знайти суми чисел від A до B і від B до C, якщо дано числа
A, B, C."""

a = int(input())
b = int(input())
c = int(input())

def two(a, b, s=0):
    if a>b:
        return 0
    else:
     for i in range(a,b+1):
      s = s + i
     return s

def tree(a,b,c,s=0, ss=0):
        for h in range(b,c):
          ss=ss+h
        return ss



print(two(a,b))
print(tree(a,b,c))
