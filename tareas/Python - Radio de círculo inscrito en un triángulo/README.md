# Diplomado TI para la innovación y el desarrollo 2022

**Módulo 3: Cómputo numérico en Python**

**Python - Radio de círculo inscrito en un triángulo**

**Presenta:**
Juan Leonardo González Elizondo

**Facilitador:**
María Andrade Aréchiga

## Código fuente de la práctica

~~~
import math

a = input("Lado A = ")
b = input("Lado B = ")
c = input("Lado C = ")

a = float(a)
b = float(b)
c = float(c)

s = (a + b + c)/2
st = math.sqrt(s\*(s-a)\*(s-b)\*(s-c))
r = st/s

print("\nEl radio del círculo inscrito dentro del triángulo (con área de " + str(st) + ") es de " + str(r))
~~~

## Aplicación en ejecución

|![](Aspose.Words.a5603208-40ca-4999-b2ab-4321fb55f79e.002.png)|
| :-: |
|*Figura 1. Código ejecutado con Spyder*|
|<p></p><p>![](Aspose.Words.a5603208-40ca-4999-b2ab-4321fb55f79e.003.png)</p>|
|*Figura 2. Cálculo de ecuación con mismos valores en Keisan Online Calculator de CASIO* |

