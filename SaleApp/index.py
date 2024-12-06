import math

import cloudinary.uploader
from flask_login import login_user, current_user, logout_user
from flask import render_template, request, redirect
import dao, admin
from __init__ import app, login
from cloudinary import uploader


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
def login_my_user():
    if current_user.is_authenticated:
        return redirect("/")

    err_msg = None
    if(request.method.__eq__('POST')):
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user)
            return redirect('/')
        else:
            err_msg = "Tài khoản hoặc mật khẩu không đúng!"
    return render_template("login.html", err_msg=err_msg)


@app.route('/logout')
def logout_my_user():
    logout_user()
    return redirect("/login")


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id=user_id)


@app.route('/register', methods=['get', 'post'])
def register_usr():
    err_msg = None
    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if password.__eq__(confirm):
            name = request.form.get('name')
            username = request.form.get('username')
            avatar = request.files.get('avatar')
            avatar_path = None

            if avatar:
                res = cloudinary.uploader.upload(avatar)
                avatar_path = res['secure_url']

            dao.add_user(name=name, username=username, password=password, avatar=avatar_path)
            return redirect("/login")
        else:
            err_msg = "Mật khẩu không khớp"

    return render_template("register.html", err_msg=err_msg)


@app.context_processor
def common_attributes():
    return {
        "categories": dao.load_categories()
    }


if __name__ == '__main__':
    app.run(debug=True)