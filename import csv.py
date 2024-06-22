import csv

#Funcion para leer el archivo CSV
def leer_archivo():
    with open(r"C:\Users\bmiranda\Prueba_3\asistencia_alumnos.csv", newline='') as archivo:
        reader = csv.reader(archivo, delimiter=";")
        return list(reader)
    
#Funcion para consultar la asistencia de los alumnos
def consultar_asistencia(rut, datos):
    for row in datos:
        if row[1] == rut:
            total_clases = int(row[5]) + int(row[6]) + int(row[7]) #Se suman los valores de las filas
            asistencia = (int(row[5]) / total_clases) *100 #Se divide el valor "presente" por el total de las clases
            print(f"La asistencia actual de {row[3]}, {row[4]} es: {asistencia}%")
            return
    print("Rut no encontrado")
    
#Funcion para visualizar la asistencia baja de los alumnos
def visualizar_asistencia_baja(datos):
    for row in datos:
        total_clases = int(row[5]) + int(row[6]) + int(row[7])
        asistencia = (int(row[5]) / total_clases) * 100
        if asistencia < 70:
            print(f"{row[3]}, {row[4]} tiene una asistencia actual de: {asistencia}%")

#Funcion para visualizar la baja asistencia
def visualizar_asistencia_baja_seccion(datos, seccion):
    contador = 0
    for row in datos:
        if row[2] == seccion:
            total_clases = int(row[5]) + int(row[6]) + int(row[7])
            asistencia = (int(row[5]) / total_clases) * 100
            if asistencia < 70:
                contador += 1
    print(f"Hay {contador} alumnos con asistencia actual menor al 70% en la sección {seccion}")

#Funcion para generar un archivo de salida con los datos obtenidos
def generar_archivo_salida(datos, seccion):
    with open(f"asistencia_{seccion}.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo, delimiter=";")
        writer.writerow(["Rut", "Nombre", "Apellido", "Asistencia Actual"])
        for row in datos:
            if row[2] == seccion:
                total_clases = int(row[5]) + int(row[6]) + int(row[7])
                asistencia = (int(row[5]) / total_clases) *100
                writer.writerow([row[1], row[3], row[4], asistencia])

#Funcion para salir del programa
def salir_del_programa():
    print("Hasta luego!")
    
#Funcion donde se almacena el menu de opciones del programa   
def menu_principal():
    datos = leer_archivo()
    opciones = {
        "1": "Consultar asistencia actual de un alumno",
        "2": "Visualizar alumnos con asistencia menor al 70%",
        "3": "Visualizar número de alumnos con asistencia menor al 70% en una sección",
        "4": "Generar archivo de salida de alumnos con asistencia en una sección",
        "5": "Salir del Programa"
    }
    opcion = input("""1: Consultar asistencia actual de un alumno 
2: Visualizar alumnos con asistencia menor al 70%
3: Visualizar número de alumnos con asistencia menor al 70% en una sección
4: Generar archivo de salida de alumnos con asistencia en una sección
5: Salir del Programa
:""")
    while opcion not in opciones:
        print("Opción incorrecta, vuelva a intentarlo.")
        opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        rut_alumno = input("Ingrese el Rut del alumno: ")
        consultar_asistencia(rut_alumno, datos)
    elif opcion == "2":
        visualizar_asistencia_baja(datos)
    elif opcion == "3":
        seccion = input("Ingrese la sigla de la sección: ")
        visualizar_asistencia_baja_seccion(datos, seccion)
    elif opcion == "4":
        seccion = input("Ingrese la sigla de la sección: ")
        generar_archivo_salida(datos, seccion)
    else:
        salir_del_programa()

menu_principal()