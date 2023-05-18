from flask import Flask, jsonify, request, abort
from products import products

app = Flask(__name__)

# Ruta de Prueba
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong!"})

# Obtener todos los productos
@app.route("/products")
def get_products():
    return jsonify({"products": products, "message":"Product's List"})

# Obtener los datos de un producto en especifico
@app.route("/products/<string:product_name>")
def get_product(product_name):
    product_found = [product for product in products if product["name"] == product_name]
    if len(product_found) > 0:
        return jsonify({"product":product_found[0]})
    else:
        abort(404)

"""
- Agregar un producto nuevo
- Se tiene que definir en el body de la request
un objeto JSON con los atributos "name", "price",
y "quantity" para poder insertarlos en la lista
de productos
"""
@app.route('/products', methods=['POST'])
def add_product():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    # print(request.json)
    return jsonify({"message":"Product added successfully!", "products": products})

# Actualizar un producto existente
# Se usa el metodo PUT para poder actualizar el registro
# OJO, solo actualizar en memoria.
# Si el server se cae, todos los productos agregados y/o actualizados
# seran eliminados (excepto los 3 originales)
@app.route('/products/<string:product_name>', methods=['PUT'])
def edit_product(product_name):
    product_found = [product for product in products if product["name"] == product_name]
    if len(product_found) > 0:
        product_found[0]["name"] = request.json["name"]
        product_found[0]["price"] = request.json["price"]
        product_found[0]["quantity"] = request.json["quantity"]
        return jsonify({
            "message" : "Product updated successfully",
            "product": product_found[0]
        })
    else:
        abort(404)

# Eliminar producto
@app.route('/products/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
    product_found = [product for product in products if product["name"] == product_name]
    if len(product_found) > 0:
        products.remove(product_found[0])
        return jsonify({
            "message": "Product Deleted!",
            "products": products
        })
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=5000)