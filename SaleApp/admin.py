from flask_admin import Admin
from __init__ import app, db
from flask_admin.contrib.sqla import ModelView
from models import Category, Product

admin = Admin(app=app, name="E-commerce Website", template_mode="bootstrap4")


class MyCategoryView(ModelView):
    column_list = ["name", "products"]
    column_searchable_list = ["name"]


class MyProductView(ModelView):
    column_list = ["name", "price", "category", "active"]
    column_searchable_list = ["name"]
    column_filters = ["name", "active", "category.id"]
    can_export = True


admin.add_views(MyCategoryView(Category, db.session))
admin.add_views(MyProductView(Product, db.session))
