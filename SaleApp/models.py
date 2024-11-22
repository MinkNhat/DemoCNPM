from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from __init__ import app, db
import hashlib


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    avatar = Column(String(255), default="https://res.cloudinary.com/dbmwgavqz/image/upload/v1727877793/uploads/ouyxa1uoesbc0ar5w8ok.jpg")

    def __str__(self):
        return self.name


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    active = Column(Boolean, default=True)
    products = relationship('Product', backref="category", lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(255), default="https://res.cloudinary.com/dbmwgavqz/image/upload/v1727877793/uploads/ouyxa1uoesbc0ar5w8ok.jpg")
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        # tao bang
        # db.create_all()

        # c1 = Category(name="MÁY ẢNH")
        # c2 = Category(name="MÁY QUAY PHIM")
        # c3 = Category(name="ỐNG KÍNH")
        # db.session.add_all([c1, c2, c3])

        # with open("data/products.json", encoding="utf-8") as f:
        #     products = json.load(f)
        #     for p in products:
        #         prod = Product(**p)
        #         db.session.add(prod)

        name = "Minh Nhat"
        username = "admin"
        password = str(hashlib.md5("123".encode('utf-8')).hexdigest())
        user = User(name=name, username=username, password=password)
        db.session.add(user)

        db.session.commit()





