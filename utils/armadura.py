import numpy as np

def matriz_rigidez_local(E, A, xi, yi, xj, yj):
    L = np.sqrt((xj - xi)*2 + (yj - yi)*2)
    lx = (xj - xi) / L
    ly = (yj - yi) / L

    k = E * A / L
    k_local = k * np.array([
        [lx*2, lx*ly, -lx*2, -lx*ly],
        [lx*ly, ly*2, -lx*ly, -ly*2],
        [-lx*2, -lx*ly, lx*2, lx*ly],
        [-lx*ly, -ly*2, lx*ly, ly*2]
    ])

    return k_local

def ensamblar_matriz_global(nodos, elementos, nodos_restringidos,F_ext,E,A):
    # Obtener el número total de nodos y grados de libertad
    num_nodos = len(nodos)
    num_grados_libertad = 2 * num_nodos

    # Inicializar la matriz global
    K_global = np.zeros((num_grados_libertad, num_grados_libertad))
    F_ext_vector = np.zeros(num_grados_libertad)
    
    
   # Calcular matrices de rigidez local para cada elemento
    for (nodo_i, nodo_j), elemento_id in elementos:
        xi, yi = nodos[nodo_i]
        xj, yj = nodos[nodo_j]
        
        k_local = matriz_rigidez_local(E, A, xi, yi, xj, yj)

        # Imprimir información del elemento y su matriz de rigidez local
        print(f"Elemento {elemento_id}:")
        print(f"Matriz de rigidez local para el elemento ({nodo_i}, {nodo_j}):")
        print(k_local)

        # Obtener los índices de los grados de libertad asociados a los nodos del elemento
        indices_i = [2 * (int(nodo_i) - 1), 2 * (int(nodo_i) - 1) + 1]
        indices_j = [2 * (int(nodo_j) - 1), 2 * (int(nodo_j) - 1) + 1]

        # Ensamblar la matriz local en la matriz global
        for i in range(2):
            for j in range(2):
                K_global[indices_i[i], indices_i[j]] += k_local[i, j]
                K_global[indices_i[i], indices_j[j]] += k_local[i, j]
                K_global[indices_j[i], indices_i[j]] += k_local[i, j]
                K_global[indices_j[i], indices_j[j]] += k_local[i, j]

    # Aplicar condiciones de restricción
    for nodo, restricciones in nodos_restringidos.items():
        idx = 2 * (int(nodo) - 1)
        for restriccion in restricciones:
            K_global[idx + restriccion, :] = 0
            K_global[:, idx + restriccion] = 0
            K_global[idx + restriccion, idx + restriccion] = 1
    
    
    # Aplicar fuerzas externas
    for i, fuerza in enumerate(F_ext):
       F_ext_vector[i] = fuerza

    # Resolver el sistema de ecuaciones
    desplazamientos = np.linalg.solve(K_global, F_ext_vector)

    return K_global, F_ext_vector, desplazamientos


# Definir datos de ejemplo
E = 20000000  # Módulo de elasticidad en Pascales
A = 0.00236  # Área transversal en metros cuadrados

# Definimos los nodos (coordenadas)
nodos = {
    '1': (0, 0),
    '2': (1.5, 0),
    '3': (1.5, 1),
    '4': (3, 0),
    '5': (3, 2)
}

# Definimos los elementos conectando nodos
elementos = [
    (('1', '2'), 1),
    (('1', '3'), 2),
    (('2', '3'), 3),
    (('2', '4'), 4),
    (('3', '4'), 5),
    (('3', '5'), 6),
    (('4', '5'), 7)
]

# Nodos restringidos (grados de libertad fijos)
nodos_restringidos = {
    '4': (1, 1),
    '5': (1, 1)
}

# Fuerzas externas aplicadas en los nodos (en Newtons)
F_ext = np.array([0, -13, 0, -19, 0, 0, 0, 0, 0, 0])

# Llamar a la función para obtener la matriz de rigidez global
