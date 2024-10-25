from flask import Flask, render_template, request
import dao

app = Flask(__name__)


# Định tuyến domain
@app.route("/")
def index():
    categories = dao.load_categories()

    q = request.args.get("q")
    category_id = request.args.get("category_id")
    products = dao.load_products(q, category_id)

    return render_template("index.html", categories=categories, products=products)


if __name__ == '__main__':
    app.run(debug=True)