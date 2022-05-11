print("2. Dados: (-2, 4), (-1, -2), (3, 5) y (4.3, 11) estimar el valor para x cuando y = 7.7")

# Función de interpolación de Lagrange de tercer grado
def int_lagrange_y_g3(x0,y0,x1,y1,x2,y2,x3,y3,x):
    l0 = ((x-x1)*(x-x2)*(x-x3))/((x0-x1)*(x0-x2)*(x0-x3))
    l1 = ((x-x0)*(x-x2)*(x-x3))/((x1-x0)*(x1-x2)*(x1-x3))
    l2 = ((x-x0)*(x-x1)*(x-x3))/((x2-x0)*(x2-x1)*(x2-x3))
    l3 = ((x-x0)*(x-x1)*(x-x2))/((x3-x0)*(x3-x1)*(x3-x2))
    
    y = ((y0)*(l0))+((y1)*(l1))+((y2)*(l2))+((y3)*(l3))
    print("\nEl resultado por interpolación de Lagrange es:\nx = " + str(y) + "\n")
#end

int_lagrange_y_g3(-2,4,-1,-2,3,5,4.3,11,7.7)