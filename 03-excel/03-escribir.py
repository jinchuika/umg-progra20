# como crear y escribir un archivo de excel
import openpyxl

book = openpyxl.Workbook()

hoja = book.active
hoja['A1'] = 'Hola'
print(hoja['A1'])

# guardar el archivo
book.save('resultado_linea7.xlsx')


# escribir fila
# filas = [
#     [88, 46, 57],
#     [89, 38, 12],
#     [23, 59, 78],
#     [56, 21, 98],
#     [24, 18, 43],
#     [34, 15, 67]
# ]

# hoja.append(['Col 1', 'Col 2', 'Col 3'])

# for fila in filas:
#     hoja.append(fila)

# book.save('resultado.xlsx')
