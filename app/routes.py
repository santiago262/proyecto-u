# app/routes.py

from flask import jsonify, request
from database.fetch_all import fetch_all_records
<<<<<<< HEAD
from database.fetch_one import fetch_one_records
from utils.helpers import calcular_fuerzas_y_momentos
=======
from database.fetch_one import fetch_one_record
from utils.helpers import calcular_fuerzas_y_momentos
from database.fetch_add import add_data
from database.fetch_remove import delete_record
>>>>>>> a9c76ab1e6dedc8b01e9d0500388a34a19bceccb

def init_routes(app):
    @app.route('/')
    def home():
        return "Bienvenido a la página de inicio"

<<<<<<< HEAD
    @app.route('/api/data', methods=['GET'])
    def get_all_data():
        data = fetch_all_records()
        return jsonify(data)

    @app.route('/api/data', methods=['POST'])
=======
    @app.route('/api/materiales', methods=['GET'])
    def get_data():
        data = fetch_all_records()
        return jsonify(data)

    @app.route('/api/viga', methods=['POST'])
>>>>>>> a9c76ab1e6dedc8b01e9d0500388a34a19bceccb
    def create_data():
        data = request.json
        print(data)

        # Asegúrate de usar las claves correctas
        P = data['P']
        L = data['L']
        ubicacion_p = data['ubicacion_p']

        # Calcular fuerzas y momentos
        resultados = calcular_fuerzas_y_momentos(P, L, ubicacion_p)

<<<<<<< HEAD
        return jsonify({'message': 'Datos creados correctamente', 'data': data, 'resultados': resultados}), 201

    @app.route('/api/data/<int:id>', methods=['GET'])
=======
        return jsonify({'message': 'Numero de materiales selecionados: {}'.format(len(data)), 'data': data, 'resultados': resultados}), 201
    @app.route('/api/materiales', methods=['POST'])
    def add_material():
        data=request.json
        register=add_data(data["nombre"],data["E"],data["densidad"],data["costo_por_kg"],data["imagen_url"])
        return jsonify(register)

    @app.route('/api/materiales/<int:id>', methods=['GET'])
>>>>>>> a9c76ab1e6dedc8b01e9d0500388a34a19bceccb
    def get_single_data(id):
        # Obtener un solo registro basado en el ID
        data = fetch_one_records(id)
        return jsonify(data)

<<<<<<< HEAD
    @app.route('/api/data/<int:id>', methods=['PUT'])
=======
    @app.route('/api/materiales/<int:id>', methods=['PUT'])
>>>>>>> a9c76ab1e6dedc8b01e9d0500388a34a19bceccb
    def update_data(id):
        data = request.json  # Obtener datos del cuerpo de la solicitud
        # Aquí podrías agregar lógica para actualizar un registro en la base de datos
        return jsonify({'message': f'Datos actualizados correctamente para el ID {id}', 'data': data})

<<<<<<< HEAD
    @app.route('/api/data/<int:id>', methods=['DELETE'])
    def delete_data(id):
        # Aquí podrías agregar lógica para eliminar un registro de la base de datos
        return jsonify({'message': f'Datos eliminados correctamente para el ID {id}'})
=======
    @app.route('/api/materiales/<int:id>', methods=['DELETE'])
    def delete_data(id):
        data=delete_record(id)
        
        return jsonify({'message': data})
>>>>>>> a9c76ab1e6dedc8b01e9d0500388a34a19bceccb
