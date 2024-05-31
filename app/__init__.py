from flask import Flask

def create_app():
    app = Flask(__name__)
    from app.routes import init_routes
    from app.routes_armadura import init_armadura
    init_armadura(app)
    init_routes(app)
    return app

