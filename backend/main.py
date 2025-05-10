from flask import Flask, jsonify, request
from flask_cors import CORS
from modules import getlistproducts
# Import the other Python file
app = Flask(__name__)
CORS(app)
@app.route('/productslist/<int:index>', methods=['GET'])
def send_products(index):
    # Call the function from the other file
    products = getlistproducts.get_products(index)
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, port=5001, )