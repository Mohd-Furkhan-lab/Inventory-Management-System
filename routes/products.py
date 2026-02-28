from flask import Blueprint
from controllers.product_controller import get_all_items_controller,get_itemby_id_controller,get_itemsby_type_controller,add_products_controller,update_products_controller,delete_products_controller
products=Blueprint("products",__name__,url_prefix="/products")

@products.route('/',methods=["GET"])
def get_products():
    return get_all_items_controller()


@products.route('/<int:id>',methods=["GET"])
def get_productsbyid(id):
    return get_itemby_id_controller(id)

@products.route('/type',methods=["GET"])
def get_products_bytype():
    return get_itemsby_type_controller()

@products.route('/',methods=["POST"])
def add_products():
    return add_products_controller()

@products.route('/<int:id>',methods=["PUT"])
def update_products(id):
    return update_products_controller()

@products.route('/<int:id>',methods=["DELETE"])
def delete_products(id):
    return delete_products_controller(id)
