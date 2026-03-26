from flask import Blueprint, request, jsonify
from app.db.session import SessionLocal
from app.services.user_service import register, login

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def reg():
    db = SessionLocal()
    data = request.json

    try:
        return jsonify(register(db, data["u"], data["e"], data["p"]))
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()


@auth_bp.route("/login", methods=["POST"])
def log():
    db = SessionLocal()
    data = request.json

    try:
        return jsonify(login(db, data["e"], data["p"]))
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()
