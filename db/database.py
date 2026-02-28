import sqlite3


def get_product_db():
    return sqlite3.connect("Products.db")

def get_admin_db():
    return sqlite3.connect("Admin.db")