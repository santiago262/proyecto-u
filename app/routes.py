# app/routes.py

from flask import jsonify, request
from database.fetch_all import fetch_all_records
from database.fetch_one import fetch_one_records
from utils.helpers import calcular_fuerzas_y_momentos

def init_routes(app):
    @app.route('/')
    def home():
        return "Bienvenido a la página de inicio"

    @app.route('/api/data', methods=['GET'])
    def get_all_data():
        data = fetch_all_records()
        return jsonify(data)

    @app.route('/api/data', methods=['POST'])
    def create_data():
        data = request.json
        print(data)

        # Asegúrate de usar las claves correctas
        P = data['P']
        L = data['L']
        ubicacion_p = data['ubicacion_p']

        # Calcular fuerzas y momentos
        resultados = calcular_fuerzas_y_momentos(P, L, ubicacion_p)

        return jsonify({'message': 'Datos creados correctamente', 'data': data, 'resultados': resultados}), 201

    @app.route('/api/data/<int:id>', methods=['GET'])
    def get_single_data(id):
        # Obtener un solo registro basado en el ID
        data = fetch_one_records(id)
        return jsonify(data)

    @app.route('/api/data/<int:id>', methods=['PUT'])
    def update_data(id):
        data = request.json  # Obtener datos del cuerpo de la solicitud
        # Aquí podrías agregar lógica para actualizar un registro en la base de datos
        return jsonify({'message': f'Datos actualizados correctamente para el ID {id}', 'data': data})

    @app.route('/api/data/<int:id>', methods=['DELETE'])
    def delete_data(id):
        # Aquí podrías agregar lógica para eliminar un registro de la base de datos
        return jsonify({'message': f'Datos eliminados correctamente para el ID {id}'})
