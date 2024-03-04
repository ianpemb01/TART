import math

a = 3
b = 5.23
c = 2.153

v = math.sqrt(a**2 + b**2 + c**2)


txt = "The length of vector ({}, {}, {},) is {}."


print(txt.format(a, b, c, v))