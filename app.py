from flask import Flask, jsonify, request

app = Flask(__name__)
inventory = {}

@app.route('/stocks', methods = ['POST'])
def add_stock():
    data = request.get_json()
    name = data.get("name")
    amount = data.get("amount", 1)

    if not name or not isinstance(amount,int) or amount <= 0:
        return jsonify({"error":"Invalid input"}), 400
    inventory[name] = inventory.get(name,0) + amount
    return jsonify({name: inventory[name]}), 201

@app.route('/stocks', methods=['GET'])
def get_stocks():
    return jsonify(inventory), 200

@app.route('/stocks/<string:name>', methods=['DELETE'])
def delete_stock(name):
    if name in inventory:
        del inventory[name]
        return jsonify({"message": f"{name} deleted"}), 200
    return jsonify({"error":"item not found"}), 404

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)