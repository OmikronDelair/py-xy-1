import sympy as sym
from sympy import *

print("3. Dados: (-1, 3), (0, -7), (4, 7) y (5, 11) estimar el polinomio interpolante")

# Función de polinomio interpolante de Newton
def int_newton(x0,y0,x1,y1,x2,y2,x3,y3):
    x = sym.Symbol('x')
    
    b1 = (y1-y0)/(x1-x0)
    b2 = (((y2-y1)/(x2-x1))-((y1-y0)/(x1-x0)))/(x2-x0)
    b3 = (((((y3-y2)/(x3-x2))-((y2-y1)/(x2-x1)))/(x3-x1))-((((y2-y1)/(x2-x1))-((y1-y0)/(x1-x0)))/(x2-x0)))/(x3-x0)
    
    y = y0 + (b1*(x-x0)) + (b2*(x-x0)*(x-x1)) + (b3*(x-x0)*(x-x1)*(x-x2))
    print("\nEl polinomio interpolante de Newton es:\ny = " + str(simplify(y)) + "\n")
#end

int_newton(-1,3,0,-7,4,7,5,11)