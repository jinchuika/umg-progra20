# librerias para correos
import smtplib, ssl
import getpass
# libreria para excel
import openpyxl

# leer el archivo
book = openpyxl.load_workbook('planilla.xlsx', data_only=True)
# fijar la hoja
hoja = book.active

celdas = hoja['A2' : 'D4']

lista_empleados = []

for fila in celdas:
    empleado = [celda.value for celda in fila]
    lista_empleados.append(empleado)

username = input("Ingrese su nombre de usuario: ")
password = getpass.getpass("Ingrese su password: ")

# Crear la conexión
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username, password)
    print("Inició sesión!")

    for empleado in lista_empleados:
        destinatario = empleado[3]
        mensaje = f'Hola {empleado[0]}, este mes ganaste {empleado[2]}'
        server.sendmail(username, destinatario, mensaje)
        print("Mensaje enviado")
