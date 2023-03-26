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

uso_servicio = [[True, False, True, False, False, False, False, True, False, False ],
                [True, False, False, True, True, True, False, False, True, False],
                [True, False, True, False, True, False, False, False, False, False],
                [True, True, True, False, False, False, False, True, False, False],
                [True, True, True, True, False, True, False, True, False, False],
                [True, False, True, False, False, True, False, True, False, False],
                [True, False, False, True, True, False, False, False, True, False],
                [True, False, True, True, False, True, False, True, True, False],
                [True, True, False, True, False, True, False, True, False, False],
                [True, True, True, False, False, True, True, True, False, False]]

tarifa_sin_uso = 10000
tarifa_con_uso = 15000

costo_mariana = 0
costo_sofia = 0
costo_camila = 0
costo_maria = 0
costo_juan = 0
costo_angie = 0
costo_esteban = 0
costo_jose = 0
costo_gisell = 0
costo_cristian = 0

for dia in range(10):
    num_usuarios = 0
    if uso_servicio[0][dia]:
        num_usuarios += 1
    if uso_servicio[1][dia]:
        num_usuarios += 1
    if uso_servicio[2][dia]:
        num_usuarios += 1
    if uso_servicio[3][dia]:
        num_usuarios += 1
    if uso_servicio[4][dia]:
        num_usuarios += 1
    if uso_servicio[5][dia]:
        num_usuarios += 1
    if uso_servicio[6][dia]:
        num_usuarios += 1
    if uso_servicio[7][dia]:
        num_usuarios += 1
    if uso_servicio[8][dia]:
        num_usuarios += 1
    if uso_servicio[9][dia]:
        num_usuarios += 1
    
    if num_usuarios == 0:
        costo_mariana += tarifa_sin_uso / 10
        costo_sofia += tarifa_sin_uso / 10
        costo_camila += tarifa_sin_uso / 10
        costo_maria += tarifa_sin_uso / 10
        costo_juan += tarifa_sin_uso / 10
        costo_angie += tarifa_sin_uso / 10
        costo_esteban += tarifa_sin_uso / 10
        costo_jose += tarifa_sin_uso / 10
        costo_gisell += tarifa_sin_uso / 10
        costo_cristian += tarifa_sin_uso / 10
    else:
        costo_por_usuario = tarifa_con_uso / num_usuarios
        if uso_servicio[0][dia]:
            costo_mariana += costo_por_usuario
        if uso_servicio[1][dia]:
            costo_sofia += costo_por_usuario
        if uso_servicio[2][dia]:
            costo_camila += costo_por_usuario
        if uso_servicio[3][dia]:
            costo_maria += costo_por_usuario
        if uso_servicio[4][dia]:
            costo_juan += costo_por_usuario
        if uso_servicio[5][dia]:
            costo_angie += costo_por_usuario
        if uso_servicio[6][dia]:
            costo_esteban += costo_por_usuario
        if uso_servicio[7][dia]:
            costo_jose += costo_por_usuario
        if uso_servicio[8][dia]:
            costo_gisell += costo_por_usuario
        if uso_servicio[9][dia]:
            costo_cristian += costo_por_usuario
diccionarioPagos ={
    "Mariana": round(costo_mariana, 2),
    "Sofia": round(costo_sofia, 2),
    "Camila": round(costo_camila, 2),
    "Maria": round(costo_maria, 2),
    "Juan": round(costo_juan, 2),
    "Angie": round(costo_angie, 2),
    "Esteban": round(costo_esteban, 2),
    "Jose": round(costo_jose, 2),
    "Gisell": round(costo_gisell, 2),
    "Cristian": round(costo_cristian, 2),
}

""""" Ejercicio 3
"""""

salario_base = 1200000
comisiones = {
    "Pantalon": 38000*0.03,
    "Zapatos": 55500*0.05,
    "Tenis": 71000*0.04,
    "Camisas": 29500*0.02,
    "Corbatas": 25000*0.07,
    "Blusas": 80500*0.05,
    "Vestidos": 95000*0.02
}
ventas = {
    "001":{"Zapatos":20,"Tenis":22,"Camisas":30,"Corbatas":2,"Pantalon":40,"Blusas":20,"Vestidos":3},
    "002":{"Zapatos":31,"Tenis":14,"Camisas":32,"Corbatas":15,"Pantalon":13,"Blusas":20,"Vestidos":11},
    "010":{"Zapatos":24,"Tenis":32,"Camisas":40,"Corbatas":9,"Pantalon":12,"Blusas":50,"Vestidos":13},
    "020":{"Zapatos":42,"Tenis":12,"Camisas":33,"Corbatas":24,"Pantalon":22,"Blusas":32,"Vestidos":23},
    "021":{"Zapatos":51,"Tenis":21,"Camisas":25,"Corbatas":10,"Pantalon":19,"Blusas":14,"Vestidos":2},
    "022":{"Zapatos":22,"Tenis":31,"Camisas":51,"Corbatas":21,"Pantalon":35,"Blusas":15,"Vestidos":11},
    "023":{"Zapatos":21,"Tenis":36,"Camisas":22,"Corbatas":32,"Pantalon":39,"Blusas":32,"Vestidos":15},
    "024":{"Zapatos":22,"Tenis":33,"Camisas":41,"Corbatas":21,"Pantalon":43,"Blusas":31,"Vestidos":36},
    "025":{"Zapatos":33,"Tenis":31,"Camisas":20,"Corbatas":42,"Pantalon":33,"Blusas":42,"Vestidos":35},
    "031":{"Zapatos":22,"Tenis":47,"Camisas":5,"Corbatas":28,"Pantalon":37,"Blusas":31,"Vestidos":32},
    "032":{"Zapatos":24,"Tenis":38,"Camisas":33,"Corbatas":21,"Pantalon":41,"Blusas":31,"Vestidos":16},
    "033":{"Zapatos":21,"Tenis":18,"Camisas":32,"Corbatas":37,"Pantalon":39,"Blusas":22,"Vestidos":12},
    "041":{"Zapatos":33,"Tenis":31,"Camisas":21,"Corbatas":21,"Pantalon":33,"Blusas":39,"Vestidos":25},
    "042":{"Zapatos":25,"Tenis":39,"Camisas":20,"Corbatas":48,"Pantalon":15,"Blusas":30,"Vestidos":32},
    "043":{"Zapatos":27,"Tenis":32,"Camisas":29,"Corbatas":28,"Pantalon":37,"Blusas":35,"Vestidos":16},
    "121":{"Zapatos":24,"Tenis":12,"Camisas":31,"Corbatas":21,"Pantalon":39,"Blusas":32,"Vestidos":13},
    "122":{"Zapatos":31,"Tenis":31,"Camisas":50,"Corbatas":22,"Pantalon":13,"Blusas":30,"Vestidos":21},
    "123":{"Zapatos":23,"Tenis":35,"Camisas":35,"Corbatas":39,"Pantalon":31,"Blusas":19,"Vestidos":19},
    "351":{"Zapatos":26,"Tenis":36,"Camisas":39,"Corbatas":27,"Pantalon":35,"Blusas":32,"Vestidos":16},
    "352":{"Zapatos":25,"Tenis":31,"Camisas":21,"Corbatas":21,"Pantalon":25,"Blusas":37,"Vestidos":15},
    "353":{"Zapatos":23,"Tenis":34,"Camisas":35,"Corbatas":32,"Pantalon":37,"Blusas":20,"Vestidos":49},
    "368":{"Zapatos":31,"Tenis":14,"Camisas":29,"Corbatas":39,"Pantalon":25,"Blusas":37,"Vestidos":16},
    "369":{"Zapatos":26,"Tenis":31,"Camisas":31,"Corbatas":27,"Pantalon":37,"Blusas":32,"Vestidos":41},
    "461":{"Zapatos":40,"Tenis":42,"Camisas":23,"Corbatas":11,"Pantalon":21,"Blusas":15,"Vestidos":19},
    "466":{"Zapatos":27,"Tenis":31,"Camisas":39,"Corbatas":21,"Pantalon":31,"Blusas":32,"Vestidos":25},
    "469":{"Zapatos":38,"Tenis":32,"Camisas":19,"Corbatas":29,"Pantalon":35,"Blusas":50,"Vestidos":16},
}
salarios = {
    "001":0,
    "002":0,
    "010":0,
    "020":0,
    "021":0,
    "022":0,
    "023":0,
    "024":0,
    "025":0,
    "031":0,
    "032":0,
    "033":0,
    "041":0,
    "042":0,
    "043":0,
    "121":0,
    "122":0,
    "123":0,
    "351":0,
    "352":0,
    "353":0,
    "368":0,
    "369":0,
    "461":0,
    "466":0,
    "469":0,
}
for empleado in ventas:
    comision = 0
    for articulo in ventas[empleado]:
        comision += ventas[empleado][articulo] * comisiones[articulo]
    salario_final = salario_base + comision
    salarios[empleado] = salario_final
sorted_salarios = sorted(salarios.items(), key=lambda x:x[1], reverse=True)
codigosAltosSalarios = [code[0] for code in sorted_salarios[0:3]]

""""" Ejercicio 4
"""""

from math import sqrt

def calculate_distance(point1, point2):
    d2 = 0
    for i in range(3):
        d2 += (point1[i] - point2[i]) ** 2
    d = sqrt(d2)
    return d
puntos = [
    ("P1",(5, 2, 3)),
    ("P2",(4, 1, 3)),
    ("P3",(2.5, 1, 0)),
    ("P4",(0.5, 0.5, 2)),
    ("P5",(1, 2, 1)),
    ("P6",(6, 2, 1)),
    ("P7",(3, 2, 0.5)),
    ("P8",(2, 6, 1)),
    ("P9",(0, 0, 0)),
    ("P10",(2, 0, 0.5)),
    ("P11",(2, 2, 3)),
    ("P12",(2, 3, 4)),
    ("P13",(1, 1, 3)),
    ("P14",(4, 4, 4)),
    ("P15",(5, 5, 1)),
    ("P16",(1, 0.5, 1)),
    ("P17",(3, 4, 5)),
    ("P18",(3, 1, 2)),
    ("P19",(3, 9, 1)),
    ("P20",(0.5, 0.5, 6)),
]
len_points = len(puntos)
parCercano = ""
minimun_distance = None
for i in range(len_points):
    for j in range(i+1,len_points):
        distance = calculate_distance(point1=puntos[i][1], point2=puntos[j][1])
        if not minimun_distance or distance <= minimun_distance:
            minimun_distance = distance
            parCercano=f"{puntos[i][0]}-{puntos[j][0]}"
            
""""" Ejercicio 5
"""""

articulos = {
    "A001":31000,
    "A011":25000,
    "A032":43000,
    "A125":55000,
    "B001":10000,
    "B005":20000,
    "P009":30000,
    "P019":49000,
    "R001":60000,
    "W307":90000,
    "Z052":35000,
    "Z025":27000,
    "Z278":65000,
}
registros = ["P009-21Unidades", "B005-19Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades", "A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades" ]


def ventasEmpresa(registros):
    dinero_total = 0
    for venta in registros:
        data = venta.split("-")
        data[1] = int(data[1].lower().split("unidad")[0])
        dinero_total += articulos[data[0]] * data[1]
        
    return dinero_total


ventasEmpresa(registros=registros)