from flask import Flask, render_template, jsonify, request

carros = [
    {"id": "1", "marca": "mazda", "modelo": 1983},
    {"id": "2", "marca": "honda", "modelo": 1993}
]

usuarios = [
    {"id": "1", "nombre": "Juan", "email": "juan@example.com"},
    {"id": "2", "nombre": "Ana", "email": "ana@example.com"}
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/carros", methods=["GET"])
def get_carros():
    return jsonify(carros)

@app.route("/carros", methods=["POST"])
def post_carros():
    nuevo_carro = request.json
    carros.append(nuevo_carro)
    return jsonify({"mensaje": "Carro creado", "carro": nuevo_carro}), 201

@app.route("/carros/<id>", methods=["DELETE"])
def delete_carro(id):
    for car in carros:
        if car["id"] == id:
            carros.remove(car)
            return jsonify({"mensaje": f"Carro con id {id} eliminado"}), 200
    return jsonify({"error": "Carro no encontrado"}), 404

@app.route("/carros/<id>", methods=["PUT"])
def put_carro(id):
    nuevo_carro = request.json
    for idx, car in enumerate(carros):
        if car["id"] == id:
            carros[idx] = nuevo_carro
            return jsonify({"mensaje": "Carro actualizado", "carro": nuevo_carro}), 200
    return jsonify({"error": "Carro no encontrado"}), 404

@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def post_usuarios():
    nuevo_usuario = request.json
    usuarios.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario creado", "usuario": nuevo_usuario}), 201

@app.route("/usuarios/<id>", methods=["DELETE"])
def delete_usuario(id):
    for user in usuarios:
        if user["id"] == id:
            usuarios.remove(user)
            return jsonify({"mensaje": f"Usuario con id {id} eliminado"}), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

@app.route("/usuarios/<id>", methods=["PUT"])
def put_usuario(id):
    nuevo_usuario = request.json
    for idx, user in enumerate(usuarios):
        if user["id"] == id:
            usuarios[idx] = nuevo_usuario
            return jsonify({"mensaje": "Usuario actualizado", "usuario": nuevo_usuario}), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
