# Como leer un archivo de excel
import openpyxl

# leer el archivo
book = openpyxl.load_workbook('planilla.xlsx', data_only=True)
# fijar la hoja
hoja = book.active

celdas = hoja['A2' : 'D4']

lista_empleados = []

for fila in celdas:
    empleado = [celda.value for celda in fila] # comprension de listas
    lista_empleados.append(empleado)

for empleado in lista_empleados:
    print(f'El empleado {empleado[0]} es un {empleado[1]} y gana {empleado[2]}')


# for fila in celdas:
#     print([celda.value for celda in fila])
