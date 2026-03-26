from app.dao.product_dao import lock_product, get_stock, add_movement, get_history


def add_stock(db, pid, qty, uid):
    try:
        if not lock_product(db, pid):
            raise Exception("Product not found")

        add_movement(db, pid, qty, "IN", uid)
        db.commit()
        return {"msg": "added"}

    except:
        db.rollback()
        raise


def purchase(db, pid, qty, uid):
    try:
        if not lock_product(db, pid):
            raise Exception("Product not found")

        stock = get_stock(db, pid)

        if stock < qty:
            raise Exception("Insufficient")

        add_movement(db, pid, -qty, "OUT", uid)
        db.commit()

        return {"remaining": stock - qty}

    except:
        db.rollback()
        raise


def history(db, pid):
    return [
        {"qty": r.quantity_change, "type": r.movement_type}
        for r in get_history(db, pid)
    ]
