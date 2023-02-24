''' 
1) Imprimir en la terminal
    dos enteros en una misma linea
    dos flotantes en una misma linea
    dos strings en una misma linea
    dos booleanos en una misma linea
    dos listas en una misma linea
    dos tuplas en una misma linea
    un diccionario en una misma linea
    un conjunto en una misma linea
'''
print(4, 8)
print(0.8, 0.6)
print("Corozo", "3.1416")
print(2>5, "fifi" == "fifi")
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
print(a, b)
c = (1, 4)
d = (2, 3)
print(c, d)
e = {"Lunes": "Monday"}
print(e)
f = {"A", "E", "I", "O", "U"}
print(f)

"2) Resolver con los operadores que considere conveniente"

""" Dadas las coordenadas P1(5,4,5) y P2(0,10,9).
Realice un codigo que determine la distancia entre ambos puntos """

import math

def distancia_entre_puntos(x1, y1, z1, x2, y2, z2):
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distancia

distancia = distancia_entre_puntos(5, 4, 5, 0, 10, 9)
print(distancia)



""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia. """

nota1 = float(input("Ingrese su primera nota: "))
nota2 = float(input("Ingrese su segunda nota: "))
nota3 = float(input("Ingrese su tercera nota: "))

promedio = (nota1 * 0.15) + (nota2 * 0.25) + (nota3 * 0.20)

if promedio >= 3:
    print("La materia ya está aprobada, con un promedio de ", promedio)
else:
    nota4 = (3 - promedio)/0.40
    print("Para aprobar la materia, necesitas sacar en el 4to parcial una nota de ", nota4)

""" Dos automoviles realizan una carrera. El primero de ellos acelera a razón constante de 3m/s², el segundo 
a razón de 5m/s². Si el segundo de ellos empieza su recorrido 10 segundos después que el primero ha empezado.
¿Cuanto tiempo habrá transcurrido cuando ambos se encuentran? """


""" Cuatro compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. El servicio se
prestará solo de ida.
Sin embargo, los cuatro no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre los cuatro.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
JUAN          Si        Si        No        Si    No
CAMILA        Si        Si        No        No    No
JOSE          Si        No        Si        No    No
MARIA         Si        Si        Si        No    No      
¿Cuanto debe pagar cada estudiante? """