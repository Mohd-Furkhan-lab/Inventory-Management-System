from db.product_model import additem,getallitems,getitemsbyid,getitemsbytype,updateitems,deleteitems

def add_items(data):
    name=data.get("name")
    price=data.get("price")
    quantity=data.get("quantity")
    type=data.get("type")
    return additem(name,price,quantity,type)

def get_allitems():
    return getallitems()

def get_itemby_id(id):
    return getitemsbyid(id)

def get_itemsby_type(data):
    type=data.get("type")
    return getitemsbytype(type)

def update_items(id,data):
    quantity=data.get("quantity")
    price=data.get("price")
    return updateitems(id,price,quantity)

def delete_item(id):
    return deleteitems(id)
