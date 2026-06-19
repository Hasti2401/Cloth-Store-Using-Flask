from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {
        "name": "Black T-Shirt",
        "price": 799,
        "category": "Men",
        "cloth_type": "T-Shirt",
        # "image": "/static/images/tshirt.jpg"
    },
    {
        "name": "Blue Jeans",
        "price": 1299,
        "category": "Men",
        "cloth_type": "Jeans",
        # "image": "/static/images/jeans.jpg"
    },
    {
        "name": "Summer Kurti",
        "price": 999,
        "category": "Women",
        "cloth_type": "Kurti",
        # "image": "/static/images/kurti.jpg"
    },
    {
        "name": "Women's Jacket",
        "price": 1999,
        "category": "Women",
        "cloth_type": "Jacket",
        # "image": "/static/images/jacket.jpg"
    },
    {
        "name": "Shirt",
        "price": 999,
        "category": "Men",
        "cloth_type": "Shirt",
        # "image": "/static/images/tshirt.jpg"
    },
    {
        "name": "T-Shirt",
        "price": 799,
        "category": "Men",
        "cloth_type": "T-Shirt",
        # "image": "/static/images/tshirt.jpg"
    },
    {
        "name": "Saree",
        "price": 1399,
        "category": "Women",
        "cloth_type": "Saree",
        # "image": "/static/images/tshirt.jpg"
    },
    {
        "name": "Kurti",
        "price": 599,
        "category": "Women",
        "cloth_type": "Kurti",
        # "image": "/static/images/tshirt.jpg"
    },
    {
        "name": "Jeans",
        "price": 799,
        "category": "Men",
        "cloth_type": "Jeans",
        # "image": "/static/images/tshirt.jpg"
    },
    {
        "name": "Hoodie",
        "price": 799,
        "category": "Men",
        "cloth_type": "Hoodie",
        # "image": "/static/images/tshirt.jpg"
    },
    {
        "name": "T-shirt",
        "price": 699,
        "category": "Women",
        "cloth_type": "T-Shirt",
        # "image": "/static/images/tshirt.jpg"
    },
    {
        "name": "Shirt",
        "price": 599,
        "category": "Womeen",
        "cloth_type": "Shirt",
        # "image": "/static/images/tshirt.jpg"
    },
]


@app.route("/", methods=["GET"])
def home():

    search = request.args.get("search", "")
    category = request.args.get("category", "")
    sort = request.args.get("sort", "")

    filtered_products = []

    for p in products:

        if search and search.lower() not in p["name"].lower():
            continue

        if category and p["category"] != category:
            continue

        filtered_products.append(p)

    if sort == "low":
        filtered_products.sort(
            key=lambda x: x["price"]
        )

    elif sort == "high":
        filtered_products.sort(
            key=lambda x: x["price"],
            reverse=True
        )


    return render_template("index.html", products=filtered_products, search=search,category=category,sort=sort)


if __name__ == "__main__":
    app.run(debug=True)