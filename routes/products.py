from flask import Blueprint
from controllers.product_controller import get_all_items_controller,get_itemby_id_controller,get_itemsby_type_controller,add_products_controller,update_products_controller,delete_products_controller
from middelwares.auth_middelware import is_login
products=Blueprint("products",__name__,url_prefix="/products")

@products.route('/',methods=["GET"])
@is_login
def get_products():
    return get_all_items_controller()

@products.route('/<int:id>',methods=["GET"])
@is_login
def get_productsbyid(id):
    return get_itemby_id_controller(id)

@products.route('/type',methods=["GET"])
@is_login
def get_products_bytype():
    return get_itemsby_type_controller()

@products.route('/',methods=["POST"])
@is_login
def add_products():
    return add_products_controller()

@products.route('/<int:id>',methods=["PUT"])
@is_login
def update_products(id):
    return update_products_controller()

@products.route('/<int:id>',methods=["DELETE"])
@is_login
def delete_products(id):
    return delete_products_controller(id)
