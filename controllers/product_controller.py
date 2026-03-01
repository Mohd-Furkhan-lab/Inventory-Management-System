from flask import request,render_template
from services.products_services import add_items,update_items,delete_item,get_allitems,get_itemsby_type,get_itemby_id

def add_products_controller():
    if request.method == "POST":
        data=request.form.to_dict()
        res= add_items(data)
        return render_template("index.html",response=res)
    return render_template("index.html")

def update_products_controller():
    if request.method == "POST":
        data=int(request.form.to_dict())
        return update_items(data)

def delete_products_controller():
    if request.method == "POST":
        id=request.form.get("id")
        return delete_item(id)

def get_all_items_controller():
    items= get_allitems()
    return render_template("index.html",data=items)

def get_itemsby_type_controller():
    type=request.args.get("name")
    data= get_itemsby_type(type)
    return render_template("index.html",data=data)

def get_itemby_id_controller():
    id=request.form.to_dict()
    items=get_itemby_id(id)
    data=[items]
    return render_template("index.html",data=data)
