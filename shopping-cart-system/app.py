
import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# In-memory cart data
cart = []

@app.route('/')
def home():
    print(f"Templates folder: {os.path.join(app.root_path, 'templates')}")
    return render_template('index.html')

@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify(cart)

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    for item in cart:
        if item['name'] == data['name']:
            item['quantity'] += 1
            return jsonify(cart)
    cart.append({**data, "quantity": 1})
    return jsonify(cart)

@app.route('/cart', methods=['PUT'])
def update_cart():
    data = request.json
    for item in cart:
        if item['name'] == data['name']:
            item['quantity'] = data['quantity']
            if item['quantity'] <= 0:
                cart.remove(item)
            break
    return jsonify(cart)

@app.route('/cart', methods=['DELETE'])
def remove_from_cart():
    data = request.json
    global cart
    cart = [item for item in cart if item['name'] != data['name']]
    return jsonify(cart)

if __name__ == '__main__':
    app.run(debug=True)
