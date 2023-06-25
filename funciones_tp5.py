
from data_stark import*
import re
import json
import os


def stark_normalizar_datos(lista: list, primera_key: str) -> None:
    for personaje in lista:
        personaje[primera_key] = float(personaje[primera_key])



########### PRIMERA PARTE #############

def imprimir_dato(dato):
    print(dato)

def imprimir_menu_desafio_5()->None:
    dato="""X. Normalizar datos
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con ‘No Tiene’).
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia
Z. Salir"""
    imprimir_dato(dato)

def stark_menu_principal_desafio_5()->str:
    imprimir_menu_desafio_5()

    opcion=input("elija opcion: ")
    opcion=opcion.upper()
    patron = re.compile("[A-Z]{1}")
    coincidencia = patron.match(opcion)

    if coincidencia == None:
        return -1
    else:
        return opcion
    

def stark_marvel_app_5(lista):
    flag=False
    while True:
        os.system("cls")
        opcion=stark_menu_principal_desafio_5()
        opcion=opcion.upper()

        if opcion == "X":
            stark_normalizar_datos(lista, "altura")
            flag=True
        elif opcion == "A":
            if flag==True:
                stark_guardar_heroe_genero(lista, "M")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "B":
            if flag==True:
                stark_guardar_heroe_genero(lista, "F")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "C":
            if flag==True:
                stark_calcular_imprimir_heroe_genero(lista, "maximo", "altura", "M")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "D":
            if flag==True:
                stark_calcular_imprimir_heroe_genero(lista, "maximo", "altura", "F")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "E":
            if flag==True:
                stark_calcular_imprimir_heroe_genero(lista, "minimo", "altura", "M")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "F":
            if flag==True:
                stark_calcular_imprimir_heroe_genero(lista, "minimo", "altura", "F")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "G":
            if flag==True:
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista, "M")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "H":
            if flag==True:
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista, "F")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "I":
            if flag==True:
                print("Heroe maculino mas alto: ")
                print(calcular_max_genero(lista, "altura", "M"))
                print("Heroe femenino mas alto: ")
                print(calcular_max_genero(lista, "altura", "F"))
                print("Heroe maculino mas bajo: ")
                print(calcular_min_genero(lista, "altura", "M"))
                print("Heroe femenino mas bajo: ")
                print(calcular_min_genero(lista, "altura", "F"))
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "J":
            if flag==True:
                stark_calcular_cantidad_por_tipo(lista, "color_ojos")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "K":
            if flag==True:
                stark_calcular_cantidad_por_tipo(lista, "color_pelo")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "L":
            if flag==True:
                stark_calcular_cantidad_por_tipo(lista, "inteligencia")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "M":
            if flag==True:
                stark_listar_heroes_por_dato(lista, "color_ojos")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "N":
            if flag==True:
                stark_listar_heroes_por_dato(lista, "color_pelo")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "O":
            if flag==True:
                stark_listar_heroes_por_dato(lista, "inteligencia")
            else:
                print("primero normalizar datos (opcion X).")
        elif opcion == "Z":
            break
        os.system("pause")


def leer_archivo(nombre_archivo:str)->dict:
    with open(nombre_archivo, 'r') as file:
        contenido = file.read()
        lista_heroes = json.loads(contenido)
        return lista_heroes

def guardar_archivo(nombre_archivo:str, contenido:str)->bool:
    try:
        with open(nombre_archivo, 'w+') as archivo:
            archivo.write(contenido)
        print(f"Se creó el archivo: {nombre_archivo}")
        return True
    except Exception:
        print(f"Error al crear el archivo '{nombre_archivo}'")
        return False


def capitalizar_palabras(cadena:str)->str:
    lista_palabras = []
    palabras = cadena.split()
    for palabra in palabras:
        palabra_capitalizada = palabra.capitalize()
        lista_palabras.append(palabra_capitalizada)
    cadena_capitalizada = ' '.join(lista_palabras)
    return cadena_capitalizada

def obtener_nombre_capitalizado(diccionario:dict)->str:
    nombre=diccionario["nombre"]
    capitalizar_nombre=capitalizar_palabras(nombre)
    return capitalizar_nombre

def obtener_nombre_y_dato(diccionario:dict, key:str)->None:
    nombre=obtener_nombre_capitalizado(diccionario)
    caracteristica=diccionario[key]
    print(f"Nombre: {nombre} | {key}: {caracteristica}")



######### SEGUNDA PARTE #######

def es_genero(diccionario:str, genero=("M" or "F" or "NB"))->bool:
    if diccionario["genero"]==genero:
        return True
    else:
        return False
    
def stark_guardar_heroe_genero(lista:list, genero:str):
    lista_nombres=[]
    for item in lista:
        if es_genero(item, genero)==True:
            nombre=obtener_nombre_capitalizado(item)
            imprimir_dato(nombre)
            lista_nombres.append(nombre)
    
    heroes = ','.join(lista_nombres)

    nombre_archivo=f"heroes_{genero}.csv"

    try:
        guardar_archivo(nombre_archivo, heroes)
        return True
    except Exception:
        return False


######### TERCERA PARTE #######

def calcular_min_genero(lista: list, key: str, genero:str) -> str:
    flag_altura = False
    for personaje in lista:
        if personaje["genero"]==genero:
            if (flag_altura == False):
                personaje_menor = personaje[key]
                nom_personaje_menor = personaje['nombre']
                flag_altura = True

            elif (personaje[key] < personaje_menor):
                personaje_menor = personaje[key]
                nom_personaje_menor = personaje['nombre']
    menor=f"Menor altura: Nombre: {nom_personaje_menor}, Altura: {personaje_menor}"
    return menor

def calcular_max_genero(lista: list, primer_key: str, genero:str) -> str:
    flag = False
    for personaje in lista:
        if personaje["genero"]==genero:
            if (flag == False):
                personaje_mayor = personaje[primer_key]
                nom_personaje_mayor = personaje['nombre']
                flag = True

            elif (personaje[primer_key] > personaje_mayor):
                personaje_mayor = personaje[primer_key]
                nom_personaje_mayor = personaje['nombre']
    mayor=f"Mayor altura: Nombre {nom_personaje_mayor}, Altura: {personaje_mayor}"
    return mayor

def calcular_max_min_dato_genero(lista:list, dato_a_realizar:str, key:str, genero:str)->str:
    if dato_a_realizar=="maximo":
        max=calcular_max_genero(lista, key, genero)
        return max
    elif dato_a_realizar=="minimo":
        min=calcular_min_genero(lista, key, genero)
        return min
    else:
        print("Debe elegir entre 'maximo' o 'minimo' a calcular")


def stark_calcular_imprimir_heroe_genero(lista:list, dato_a_realizar:str, key:str, genero:str)->str:
    nombre=calcular_max_min_dato_genero(lista, dato_a_realizar, key, genero)
    imprimir_dato(nombre)
    guardar_archivo(f"heroes_{dato_a_realizar}_{key}_{genero}.csv", nombre)



######### CUARTA PARTE #######


def sumar_dato_heroe_genero(heroes:list, key:str, genero:str):
    suma = 0

    for heroe in heroes:
        if type(heroe) == dict:
            if heroe["genero"]==genero:
                suma += heroe[key]
    return suma


def cantidad_heroes_genero(lista:list, genero:str):
    contador=0
    for heroe in lista:
        if heroe["genero"]==genero:
            contador+=1
    return contador

def dividir(dividendo:int, divisor:int)->float:  
    if divisor == 0:
        return 0
    else: 
        division=dividendo/divisor
        return division

def calcular_promedio_genero(lista: list, key: str, genero:str) -> float:
    contador=0
    acumulador=sumar_dato_heroe_genero(lista, key, genero)
    contador=cantidad_heroes_genero(lista, genero)
    promedio=dividir(acumulador,contador)
    return promedio

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista:list, genero:str):
    if len(lista)>0:
        promedio=calcular_promedio_genero(lista, "altura", genero)
        imprimir=f"Altura promedio género {genero}: {promedio}"
        imprimir_dato(imprimir)
        guardar_archivo(f"heroes_promedio_altura_{genero}.csv", imprimir)
    else:
        print("Error: Lista de héroes vacía.")
        return False


######### QUINTA PARTE #######

def calcular_cantidad_tipo(lista:list, key:str)->dict:
    tipo_dato = {}
    
    if len(lista)<=0:
        return {"error":"lista de heroes vacia"}
    
    for heroe in lista:
        if key in heroe:
            valor = heroe[key]
            capitalizar_palabras(valor)
            if valor in tipo_dato:
                tipo_dato[valor] += 1
            else:
                tipo_dato[valor] = 1
    
    return tipo_dato


def guardar_cantidad_heroes_tipo(diccionario: dict, tipo_dato: str):
    contenido = ""
    for key, value in diccionario.items():
        mensaje = f"Caracteristica: {tipo_dato} {key} - Cantidad de heroes: {value}\n"
        contenido += mensaje

    guardar_archivo(f"heroes_cantidad_{tipo_dato}.csv", contenido)

def stark_calcular_cantidad_por_tipo(lista:list, tipo_dato:str):
    dic=calcular_cantidad_tipo(lista, tipo_dato)
    guardar_cantidad_heroes_tipo(dic, tipo_dato)


######### SEXTA PARTE #######

def obtener_lista_de_tipos(lista:list, key:str)->set:
    valores=set()
    for item in lista:
        if item[key]=="" or item[key]=="":
            item[key]="N/A"
        capitalizar_palabras(item[key])
        valores.add(item[key])
    return valores

def normalizar_dato(dato:str, valor_default:str)->str:
    if dato.strip() == '':
        return valor_default
    else:
        return dato

def normalizar_heroe(diccionario:dict, key:str):
    if key in diccionario:
        diccionario[key] = capitalizar_palabras(normalizar_dato(diccionario[key], "N/A"))
    diccionario['nombre'] = capitalizar_palabras(diccionario['nombre'])
    return diccionario 


def obtener_heroes_por_tipo(heroes, tipos, tipo_dato):
    heroes_por_tipo = {}

    for tipo in tipos:
        heroes_por_tipo[tipo] = []

    for tipo in tipos:
        for heroe in heroes:
            if tipo_dato in heroe:
                valor_tipo = normalizar_dato(heroe[tipo_dato], "N/A")
                if valor_tipo == tipo:
                    heroes_por_tipo[tipo].append(heroe['nombre'])

    return heroes_por_tipo

def guardar_heroes_por_tipo(diccionario:dict, tipo_dato:str):
    contenido = ""

    for tipo, heroes in diccionario.items():
        heroes_formateados = " | ".join(heroes)
        contenido += f"{tipo_dato.capitalize()} {tipo}: {heroes_formateados}\n"

    guardar_archivo(f"heroes_segun_{tipo_dato}.csv", contenido)

def stark_listar_heroes_por_dato(lista, tipo_dato):
    tipos = obtener_lista_de_tipos(lista, tipo_dato)
    heroes_por_tipo = obtener_heroes_por_tipo(lista, tipos, tipo_dato)
    return guardar_heroes_por_tipo(heroes_por_tipo, tipo_dato)

