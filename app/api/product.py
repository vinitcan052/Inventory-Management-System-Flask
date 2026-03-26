from flask import Blueprint, request, jsonify
from app.db.session import SessionLocal
from app.services.product_service import create, list_all, get_one
from app.core.security import jwt_required

product_bp = Blueprint("product", __name__)


@product_bp.route("/", methods=["POST"])
@jwt_required
def create_p():
    db = SessionLocal()
    try:
        return jsonify(create(db, **request.json))
    finally:
        db.close()


@product_bp.route("/", methods=["GET"])
@jwt_required
def list_p():
    db = SessionLocal()
    try:
        return jsonify(list_all(db))
    finally:
        db.close()


@product_bp.route("/<int:pid>")
@jwt_required
def one(pid):
    db = SessionLocal()
    try:
        return jsonify(get_one(db, pid))
    finally:
        db.close()
