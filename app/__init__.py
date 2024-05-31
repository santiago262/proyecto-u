from flask import Flask

def create_app():
    app = Flask(__name__)
    from app.routes import init_routes
<<<<<<< HEAD
    from app.routes_armadura import init_armadura
    init_armadura(app)
=======
>>>>>>> a9c76ab1e6dedc8b01e9d0500388a34a19bceccb
    init_routes(app)
    return app

