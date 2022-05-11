print("1. Dados: (-4, -2) y (1, 5) estimar el valor para x cuando y = 3.7")

# Función de interpolación lineal para encontrar X
def int_lineal_x(x0,y0,x1,y1,y):
    x = (((x1-x0)*(y-y0))/(y1-y0))+x0
    print("\nEl resultado es:\nx = " + str(x) + "\n")
#end

int_lineal_x(-4,-2,1,5,3.7)