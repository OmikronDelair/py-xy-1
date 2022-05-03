#
# radious of circle inscribed in a tringle
# place here your solution code
#
# zeeAlso
# https://keisan.casio.com/exec/system/1223428152

import math

a = input("Lado A = ")
b = input("Lado B = ")
c = input("Lado C = ")

a = float(a)
b = float(b)
c = float(c)

s = (a + b + c)/2
st = math.sqrt(s*(s-a)*(s-b)*(s-c))
r = st/s

print("\nEl radio del círculo inscrito dentro del triángulo (con área de " + str(st) + ") es de " + str(r))