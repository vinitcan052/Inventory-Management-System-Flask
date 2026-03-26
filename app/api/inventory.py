from flask import Blueprint, request, jsonify
from app.db.session import SessionLocal
from app.services.inventory_service import add_stock, purchase, history
from app.core.security import jwt_required

inventory_bp = Blueprint("inventory", __name__)


@inventory_bp.route("/add", methods=["POST"])
@jwt_required
def add():
    db = SessionLocal()
    data = request.json

    try:
        return jsonify(add_stock(db, data["pid"], data["qty"], request.user_id))
    finally:
        db.close()


@inventory_bp.route("/buy", methods=["POST"])
@jwt_required
def buy():
    db = SessionLocal()
    data = request.json

    try:
        return jsonify(purchase(db, data["pid"], data["qty"], request.user_id))
    finally:
        db.close()


@inventory_bp.route("/history/<int:pid>")
@jwt_required
def hist(pid):
    db = SessionLocal()
    try:
        return jsonify(history(db, pid))
    finally:
        db.close()
