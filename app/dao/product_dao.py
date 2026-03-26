from sqlalchemy import func
from app.models.models import Product, StockMovement


def create_product(db, name, sku, price):
    p = Product(name=name, sku=sku, price=price)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p


def get_all_products(db):
    return db.query(Product).all()


def get_product_by_id(db, pid):
    return db.query(Product).filter(Product.id == pid).first()


def lock_product(db, pid):
    return db.query(Product).filter(Product.id == pid).with_for_update().first()


def get_stock(db, pid):
    return db.query(func.coalesce(func.sum(StockMovement.quantity_change), 0))\
        .filter(StockMovement.product_id == pid).scalar()


def add_movement(db, pid, qty, mtype, uid):
    db.add(StockMovement(
        product_id=pid,
        quantity_change=qty,
        movement_type=mtype,
        user_id=uid
    ))


def get_history(db, pid):
    return db.query(StockMovement)\
        .filter(StockMovement.product_id == pid)\
        .order_by(StockMovement.created_at.desc()).all()
