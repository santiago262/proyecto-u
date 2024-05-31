from flask import jsonify, request
import numpy as np
from utils.armadura import ensamblar_matriz_global
def init_armadura(app):
    @app.route('/api/armadura', methods=['POST'])
    def get_data():
        data=request.json
        nodos = data['nodos']
        E=data['E']
        A=data['A']
        elementos = [(tuple(par), id) for par, id in data['elementos']]
        nodos_convertidos = {k: tuple(v) for k, v in nodos.items()}
        nodos_restringidos = {k: tuple(v) for k, v in data['nodos_restringidos'].items()}
        F_ext = np.array(data['F_ext'])
        K_global, F_ext_vector, desplazamientos = ensamblar_matriz_global(nodos, elementos, nodos_restringidos, F_ext, E, A)
        return jsonify({"K_global":K_global,"F_ext_vector":F_ext_vector,"desplazamientos":desplazamientos})

