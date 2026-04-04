from app.services.admin_services import admin_login_check,add_admin
from flask import request,render_template,redirect,url_for

def login_controller():
    if request.method == "POST":
        data=request.form.to_dict()
        res=admin_login_check(data)
        if res :
            return redirect(url_for('products.get_products'))
    return render_template("login.html")

def singup_controller():
    if request.method == "POST":
        data=request.form.to_dict()
        res=add_admin(data)
        if res:
            return redirect(url_for('products.get_products'))
    return render_template("signup.html")

def logout_controller():
    if request.method == "POST":
        return redirect(url_for("admin.adminlogin"))
