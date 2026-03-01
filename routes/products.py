from flask import Blueprint
from controllers.product_controller import get_all_items_controller,get_itemby_id_controller,get_itemsby_type_controller,add_products_controller,update_products_controller,delete_products_controller
from middelwares.auth_middelware import is_login
products=Blueprint("products",__name__,url_prefix="/products")

@products.route('/',methods=["GET","POST"])
@is_login
def get_products():
    return get_all_items_controller()

@products.route('/',methods=["GET","POST"])
@is_login
def get_productsbyid():
    return get_itemby_id_controller(id)

@products.route('/type',methods=["GET","POST"])
@is_login
def get_products_bytype():
    return get_itemsby_type_controller()

@products.route('/add',methods=["POST","GET"])
@is_login
def add_products():
    return add_products_controller()

@products.route('/update',methods=["POST"])
@is_login
def update_products():
    return update_products_controller()

@products.route('/delete',methods=["POST"])
@is_login
def delete_products():
    return delete_products_controller()
