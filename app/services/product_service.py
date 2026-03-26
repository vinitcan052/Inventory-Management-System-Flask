from app.dao.product_dao import create_product, get_all_products, get_product_by_id


def create(db, name, sku, price):
    p = create_product(db, name, sku, price)
    return {"id": p.id}

from app.dao.product_dao import get_all_products, get_stock

def list_all(db):
    products = get_all_products(db)
    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "sku": p.sku,
            "price": float(p.price),  
            "units": get_stock(db, p.id) 
        })
    return result

def get_one(db, pid):
    p = get_product_by_id(db, pid)
    if not p:
        raise Exception("Not found")
    return {"id": p.id, "name": p.name}
