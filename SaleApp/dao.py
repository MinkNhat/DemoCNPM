import hashlib
from models import *


def load_categories():
    # with open("data/categories.json", encoding="utf-8") as f:
    #     return json.load(f)
    return Category.query.all()


def load_products(q=None, category_id=None, page=None):
    # with open("data/products.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #     if q:
    #         products = [p for p in products if p['name'].find(q) >= 0]
    #     if category_id:
    #         products = [p for p in products if p['category_id'] == int(category_id)]
    #     return products
    query = Product.query

    if q:
        query = query.filter(Product.name.contains(q))

    if category_id:
        query = query.filter(Product.category_id.__eq__(int(category_id)))

    if page:
        page_size = int(app.config["PAGE_SIZE"])
        start = (int(page)-1)*page_size
        query = query.slice(start, start+page_size)

    return query.all()


def load_product_by_id(id):
    # with open("data/products.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #     for p in products:
    #         if p["id"].__eq__(id):
    #             return p
    return Product.query.get(id)


def count_product():
    return Product.query.count()


if __name__ == "__main__":
    print(load_products())