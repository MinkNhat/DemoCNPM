import math

from flask import render_template, request, redirect
import dao
from __init__ import app, db


# Định tuyến domain
@app.route("/")
def index():
    q = request.args.get("q")
    category_id = request.args.get("category_id")
    page = request.args.get("page")
    products = dao.load_products(q, category_id, page)
    pages = dao.count_product()

    return render_template("index.html", products=products, pages=math.ceil(pages/app.config["PAGE_SIZE"]))


@app.route("/products/<int:id>")
def product_details(id):
    product = dao.load_product_by_id(id)
    categories = dao.load_categories()
    return render_template("product-details.html", product=product)


@app.route("/login", methods=['get', 'post'])
def login_user():
    if(request.method.__eq__('POST')):
        username = request.form.get('username')
        password = request.form.get('password')
        if username.__eq__("admin") and password.__eq__("123"):
            return redirect("/")
    return render_template("login.html")


@app.context_processor
def common_attributes():
    return {
        "categories": dao.load_categories()
    }


if __name__ == '__main__':
    app.run(debug=True)