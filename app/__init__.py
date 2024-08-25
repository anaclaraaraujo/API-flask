from flask import Flask
from app.extensions import db, login_manager, cors
from app.routes.auth import auth_bp
from app.routes.products import products_bp
from app.routes.cart import cart_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '7b5d87610094b92f92330706d6ce23d47f6d12930bca85ab8541aa264939d721'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    
    db.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(cart_bp)
    
    return app
