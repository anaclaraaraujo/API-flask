from flask import Blueprint, request, jsonify
from flask_login import login_required
from app.models import Product, db

products_bp = Blueprint('products', __name__)

@products_bp.route('/api/products/add', methods=['POST'])
@login_required
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data['name'], price=data['price'], description=data.get('description', ''))
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully'})
    return jsonify({'message': 'Invalid product data'}), 400

@products_bp.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'})
    return jsonify({'message': 'Product not found'}), 404

@products_bp.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description
        })
    return jsonify({'message': 'Product not found'}), 404

@products_bp.route('/api/products/update/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    data = request.json
    if 'name' in data:
        product.name = data['name']
    
    if 'price' in data:
        product.price = data['price']

    if 'description' in data:
        product.description = data['description']

    db.session.commit()    
    return jsonify({'message': 'Product updated successfully'})

@products_bp.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price
        } 
        for product in products
    ]

    return jsonify(product_list)
