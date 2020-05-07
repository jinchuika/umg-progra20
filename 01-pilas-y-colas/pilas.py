# importar el tipo de dato para utilizar pilas y colas
from collections import deque

# definir la pila
historial = deque()

# usar append para agregar elementos
# es el equivalente al PUSH de una cola normal
historial.append('primera acción')
historial.append('segunda acción')
historial.append('tercera acción')
historial.append('cuarta acción')

print(f"Historial actual {historial}")
print('#################')

while len(historial) > 0:
    # extraer el último elemento utilizando pop
    ultima_acction = historial.pop()

    print(f'Acción más reciente: {ultima_acction}')
    print(f'Historial actual: {historial}')
    print('#################')
