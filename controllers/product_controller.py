from flask import request,render_template,redirect,url_for
from services.products_services import add_items,update_items,delete_item,get_allitems,get_itemsby_type,get_itemby_id

def add_products_controller():
    if request.method == "POST":
        data=request.form.to_dict()
        res= add_items(data)
        return redirect(url_for("products.get_products"))
    return redirect(url_for("products.get_products"))

def update_products_controller():
    if request.method == "POST":
        data=request.form.to_dict()
        res= update_items(data)
        return redirect(url_for("products.get_products"))

def delete_products_controller():
    if request.method == "POST":
        id=request.form.get("id")
        res= delete_item(id)
        return redirect(url_for("products.get_products"))

def get_all_items_controller():
    items= get_allitems()
    return render_template("index.html",data=items)

def get_itemsby_type_controller():
    type=request.form.get("type")
    data= get_itemsby_type(type)
    return render_template("index.html",data=data)

def get_itemby_id_controller():
    id=request.form.get("id")
    items=get_itemby_id(id)
    print(items)
    return render_template("index.html",data=items)