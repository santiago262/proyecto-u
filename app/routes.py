# app/routes.py

from flask import jsonify, request
from database.fetch_all import fetch_all_records
from database.fetch_one import fetch_one_record
from utils.helpers import calcular_fuerzas_y_momentos
from database.fetch_add import add_data
from database.fetch_remove import delete_record

def init_routes(app):
    @app.route('/')
    def home():
        return "Bienvenido a la página de inicio"

    @app.route('/api/materiales', methods=['GET'])
    def get_data():
        data = fetch_all_records()
        return jsonify(data)

    @app.route('/api/viga', methods=['POST'])
    def create_data():
        data = request.json
        print(data)

        # Asegúrate de usar las claves correctas
        P = data['P']
        L = data['L']
        ubicacion_p = data['ubicacion_p']

        # Calcular fuerzas y momentos
        resultados = calcular_fuerzas_y_momentos(P, L, ubicacion_p)

        return jsonify({'message': 'Numero de materiales selecionados: {}'.format(len(data)), 'data': data, 'resultados': resultados}), 201
    @app.route('/api/materiales', methods=['POST'])
    def add_material():
        data=request.json
        register=add_data(data["nombre"],data["E"],data["densidad"],data["costo_por_kg"],data["imagen_url"])
        return jsonify(register)

    @app.route('/api/materiales/<int:id>', methods=['GET'])
    def get_single_data(id):
        # Obtener un solo registro basado en el ID
        data = fetch_one_records(id)
        return jsonify(data)

    @app.route('/api/materiales/<int:id>', methods=['PUT'])
    def update_data(id):
        data = request.json  # Obtener datos del cuerpo de la solicitud
        # Aquí podrías agregar lógica para actualizar un registro en la base de datos
        return jsonify({'message': f'Datos actualizados correctamente para el ID {id}', 'data': data})

    @app.route('/api/materiales/<int:id>', methods=['DELETE'])
    def delete_data(id):
        data=delete_record(id)
        
        return jsonify({'message': data})
