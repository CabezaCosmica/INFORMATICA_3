#====================== EJERCICIOS MÉTODOS DE LISTAS ====================

#==> EJERCICIO 1

""" Realice las siguientes operaciones sobre listas:
        * ["A","B","C"] Elimine el último elemento de la lista
                        Luego agregue su nombre al final de la lista
"""
lista=["A", "B", "C"]
lista.pop()
lista.append("Gustavo")
print(lista)
"""                  
        * [100,200,300] Elimine el segundo elemento de la lista,
                        Luego agregue su edad como segundo elemento de la lista
"""
lista1=[100, 200, 300]
lista1.pop(1)
lista1.insert(1, 21)
print(lista1)
"""
        * [1,2,3,4]     Elimine el último elemento de la lista
                        Luego agrege los valores 100, 200, 300 al final de la lista
                        Elimine el segundo elemento de la lista
                        Luego inserte el valor -1 en la segunda posición de la lista
"""
lista2=[1, 2, 3, 4]
lista2.pop()
lista2.append(100)
lista2.append(200)
lista2.append(300)
lista2.pop(1)
lista2.insert(1, -1)
print(lista2)
"""
        * Contruya una sola lista con los elementos resultantes de las 3 listas anteriores."""
lista3 = lista + lista1 + lista2
print(lista3)

#==> EJERCICIO 2

""" Determine si el numero 25 está en la lista edades,
    y si es así cuantas veces aparece.
    edades = [0,1,2,3,4,5,6,7,8,9,1,0,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9,2,0,2,1,2,2,2,3,2,4,2,5,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] """

edades = [0,1,2,3,4,5,6,7,8,9,1,0,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9,2,0,2,1,2,2,2,3,2,4,2,5,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print(edades.count(25))

#==> EJERCICIO 3
""" Teniendo en cuenta la lista anterior, ordene de forma ascendente,luego descendente a los elementos.
    Pero sin alterar la lista edades original. """

edades.sort(reverse=False)
print(edades)

edades.sort(reverse=True)
print(edades)

#==> EJERCICIO 4
""" Cree una copia de edades y haga lo siguiente:
   * Muestre en pantalla el elemento inicial y el final
   * Remueva aquellos elementos cuyo valor es 0 o 1"""
 
copia_edades = edades.copy()

print("Primer elemento de la lista copiada:", copia_edades[0])
print("Último elemento de la lista copiada:", copia_edades[-1])

copiaedades = edades.copy()
for elemento in edades:
    if elemento != 0 and elemento !=1:
        copiaedades.append(elemento)
print(copiaedades)

#==> EJERCICIO 5
"""  Utilice slicing para extraer a partir de la lista edades:
         - Elementos ubicados en indices pares
         - Elementos ubicados en indices impares
         - Todos los elementos, pero al revés de la lista
         - Cada 70avo elemento a partir del 10
         - Cada 100avo elemento, pero al revés de la lista
         - Cada 35avo elemento, a partir de la mitad
  ¿Qué operaciones puedo hacer con listas que no puede hacer con tuplas? """
