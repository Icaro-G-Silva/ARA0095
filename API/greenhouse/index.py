from flask import Flask, jsonify, request

from greenhouse.model.GreenhouseInfo import Greenhouse, GreenhouseSchema

app = Flask(__name__)

InfosMock = [Greenhouse("GH-01", "X st, 115", "123987489", 25, 80, 69, 0, 0)]


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/info", methods=["POST"])
def add_info():
    info = GreenhouseSchema().load(request.get_json())
    InfosMock.append(info)
    return "", 200


@app.route("/info")
def get_info():
    schema = GreenhouseSchema(many=True)
    infos = schema.dump(InfosMock)
    return jsonify(infos), 200


if __name__ == "__main__":
    app.run()
