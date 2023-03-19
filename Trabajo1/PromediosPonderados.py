import gurobipy as gp

# Definir grafo
# Definir nodos (n)
# nodos 1 y n son origen y destino
# Definir arcos
# Tener en cuenta qué:
# Para los arcos no repetidos, la información es valida en cualquier dirección
# Para los repetidos la información es valida solo en la dirección especificada
# Objetivos:
# 1. Minimizar la distancia total recorrida
# 2. Minimizar las emisiones totales esperadas
# 3. Minimizar el riesgo de exposición
