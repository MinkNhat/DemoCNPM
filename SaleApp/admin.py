from flask_admin import Admin, expose
from __init__ import app, db
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView
from models import Category, Product, UserEnum
from flask_login import current_user, logout_user
from flask import redirect

admin = Admin(app=app, name="E-commerce Website", template_mode="bootstrap4")


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == UserEnum.ADMIN


class MyBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyCategoryView(MyModelView):
    column_list = ["name", "products"]
    column_searchable_list = ["name"]


class MyProductView(MyModelView):
    column_list = ["name", "price", "category", "active"]
    column_searchable_list = ["name"]
    column_filters = ["name", "active", "category.id"]
    can_export = True


class StatsView(MyBaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


class LogoutView(MyBaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_views(MyCategoryView(Category, db.session))
admin.add_views(MyProductView(Product, db.session))
admin.add_views(StatsView(name='Thống Kê'))
admin.add_views(LogoutView(name='Đăng Xuất'))
