import importlib
from flask import Flask, Blueprint


app = Flask(__name__)

module = importlib.import_module("routes.blueprints")
for name, blueprint in module.__dict__.items():
    if isinstance(blueprint, Blueprint):
        importlib.import_module("routes.{}.index".format(name))
        app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(debug=True)
