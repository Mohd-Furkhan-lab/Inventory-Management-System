from services.admin_services import admin_login_check,add_admin
from flask import request

def login_controller():
    data=request.get_json()
    return admin_login_check(data)

def singup_controller():
    data=request.get_json()
    return add_admin(data)
