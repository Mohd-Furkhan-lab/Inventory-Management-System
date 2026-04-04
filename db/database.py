import sqlite3


def get_product_db():
    return sqlite3.connect("/tmp/Products.db")

def get_admin_db():
    return sqlite3.connect("/tmp/Admin.db")
