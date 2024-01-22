import importlib
from flask import Flask, Blueprint
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

module = importlib.import_module("routes.blueprints")
for name, blueprint in module.__dict__.items():
    if isinstance(blueprint, Blueprint):
        importlib.import_module("routes.{}.index".format(name))
        app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(debug=True)
