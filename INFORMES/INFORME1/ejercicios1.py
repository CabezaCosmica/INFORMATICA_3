nombre_completo = "Gustavo Adolfo López Arteaga"

"""""   Ejercicio 1
"""""
def esMayorDeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False
    
def sumadeDigitos(numero):
    suma = 0
    for i in str(numero):
        suma += int(i)
    return suma

def tieneVocales(mensaje):
    for i in mensaje:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            return True
    return False

def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero/2)+1):
        if numero % i == 0:
            return False
    return True

funciones = [esMayorDeEdad, sumadeDigitos, tieneVocales, esPrimo]

"""""   Ejercicio 2
"""""
diccionario ={
    "Daniel": 23,
    "Gustavo": 21,
    "Luis": 21
}
diccionario["Daniel"]= 24
print(diccionario.values())