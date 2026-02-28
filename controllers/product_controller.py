from flask import request
from services.products_services import add_items,update_items,delete_item,get_allitems,get_itemsby_type,get_itemby_id

def add_products_controller():
    data=request.get_json()
    return add_items(data)

def update_products_controller():
    id=int(request.args.get("id"))
    data=request.get_json()
    return update_items(id,data)

def delete_products_controller(id):
    return delete_item(id)

def get_all_items_controller():
    return get_allitems()

def get_itemsby_type_controller():
    data=request.get_json()
    return get_itemsby_type(data)

def get_itemby_id_controller(id):
    return get_itemby_id(id)
