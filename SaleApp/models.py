from sqlalchemy import Column, Integer, String
from __init__ import app, db


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        # tao bang
        # db.create_all()

        c1 = Category(name="Máy ảnh")
        c2 = Category(name="Máy quay phim")
        c3 = Category(name="Ống kính")

        db.session.add_all([c1, c2, c3])
        db.session.commit()



