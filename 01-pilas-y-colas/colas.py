# importar el tipo de dato para utilizar pilas y colas
from collections import deque

# definir la cola
cola = deque()

# agregar elementos
cola.append('primer documento.txt')
cola.append('segundo documento.txt')
cola.append('tercer documento.txt')
cola.append('cuarto documento.txt')

print(f'Cola de impresión: {cola}')
print("#########")

while len(cola) > 0:
    # extraer el primer elemento en la cola
    siguiente_elemento = cola.popleft()

    print(f'Siguiente elemento: {siguiente_elemento}')
    print(f'Cola de impresión: {cola}')
    print("#########")
