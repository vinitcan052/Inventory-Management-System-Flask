from flask import Flask,render_template
from app.api.auth import auth_bp
from dotenv import load_dotenv
from app.api.product import product_bp
from app.api.inventory import inventory_bp
from app.db.session import Base, engine
from flask_cors import CORS 

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}}) 
    
    @app.route("/")
    def home():
        return render_template("index.html")

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(product_bp, url_prefix="/products")
    app.register_blueprint(inventory_bp, url_prefix="/inventory")

    Base.metadata.create_all(bind=engine)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
