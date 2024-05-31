# database/material.py

class Material:
    def __init__(self, id, nombre, E, densidad, costo_por_kg, imagen_url):
        self.id = id
        self.nombre = nombre
        self.E = E
        self.densidad = densidad
        self.costo_por_kg = costo_por_kg
        self.imagen_url = imagen_url

    def as_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'E': self.E,
            'densidad': self.densidad,
            'costo_por_kg': self.costo_por_kg,
            'imagen_url': self.imagen_url
        }
