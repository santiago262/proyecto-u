import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from database.fetch_all import fetch_all_records

def calcular_fuerzas_y_momentos(P, L, ubicacion_p):
    # Distancias a los puntos de apoyo
    distancia_a_A = ubicacion_p
    distancia_a_B = L - ubicacion_p

    # Momentos alrededor de los puntos de apoyo
    MA = P * distancia_a_B
    MB = P * distancia_a_A
    FB = (distancia_a_A / L) * P

    # Fuerza en el punto A (en Newtons)
    FA = (distancia_a_B / L) * P
    # Imprimir resultados
    print("La fuerza en el punto A es:", FA, "N")
    print("La fuerza en el punto B es:", FB, "N")

    print("El momento alrededor del punto A es:", MA, "N.M")
    print("El momento alrededor del punto B es:", MB, "N.M")

    # Obtener los materiales de la base de datos
    materiales = fetch_all_records()

    # Asumiendo una sección transversal rectangular común para simplificar
    b = 0.4  # Base en metros
    h = 0.5  # Altura en metros
    I = (b * h**3) / 12  # Momento de inercia para una sección rectangular

    resultados_materiales = []

    for material in materiales:
        # Asegurarse de que el material tiene las propiedades necesarias
        E = material.get('E')
        nombre = material.get('nombre')
        imagen_url = material.get('imagen_url')
        
        if E is None or nombre is None:
            continue  # Saltar este material si faltan propiedades

        # Calcular la carga máxima y la deflexión
        M_max = max(MA, MB)
        sigma_max = M_max * (h / 2) / I
        delta_max = (M_max * L**2) / (8 * E * I)

        # Criterios de selección
        resistencia_material = material.get('resistencia', E / 1000)  # Usar resistencia del material o un factor de seguridad
        if delta_max < 0.01 and sigma_max < resistencia_material:
            resultados_materiales.append(material)

    return resultados_materiales

P = 100  
L = 7.0  
ubicacion_p = 2.0  

