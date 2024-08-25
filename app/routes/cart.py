from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import CartItem, Product, db

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/api/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    user = current_user
    product = Product.query.get(product_id)

    if user and product:
        cart_item = CartItem(user_id=user.id, product_id=product.id)
        db.session.add(cart_item)
        db.session.commit()
        return jsonify({'message': 'Product added to cart successfully'})
    return jsonify({'message': 'Failed to add item to the cart'}), 400

@cart_bp.route('/api/cart/remove/<int:product_id>', methods=['DELETE'])
@login_required
def remove_from_cart(product_id):
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()

    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({'message': 'Item removed from cart successfully'})
    return jsonify({'message': 'Item not found in the cart'}), 404

@cart_bp.route('/api/cart', methods=['GET'])
@login_required
def view_cart():
    user = current_user
    cart_items = user.cart
    cart_content = [
        {
            'id': cart_item.id,
            'user_id': cart_item.user_id,
            'product_id': cart_item.product_id,
            'product_name': cart_item.product.name,
            'product_price': cart_item.product.price
        }
        for cart_item in cart_items
    ]
    return jsonify(cart_content)

@cart_bp.route('/api/cart/checkout', methods=['POST'])
@login_required
def checkout():
    user = current_user
    cart_items = user.cart

    for cart_item in cart_items:
        db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'message': 'Checkout successfully. Cart has been cleared.'})
