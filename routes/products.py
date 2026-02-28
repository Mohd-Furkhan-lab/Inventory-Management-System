from flask import Blueprint
from flask import request
products=Blueprint("products",__name__,url_prefix="/products")

@products.route('/',methods=["GET"])
def get_products():
    return "All Product"


@products.route('/<int:id>',methods=["GET"])
def get_productsbyid(id):
    return f"Product {id}"

@products.route('/type',methods=["GET"])
def get_products_bytype():
    name=request.args.get("name")
    return f"{name} Products"

@products.route('/',methods=["POST"])
def add_products():
    data=request.get_json()
    name=data.get("name")
    return f"{name} Product Added"

@products.route('/<int:id>',methods=["PUT"])
def update_products(id):
    data=request.get_json()
    return f"Products {id} Updated"

@products.route('/<int:id>',methods=["DELETE"])
def delete_products(id):
    return f"Products {id} Delted"