from flask import Blueprint,session,request
from controllers.admin_controller import login_controller,singup_controller

admin=Blueprint("admin",__name__,url_prefix="/admin")

@admin.route('/login',methods=["GET","POST"])
def adminlogin():
    return login_controller()


@admin.route('/signup',methods=["GET","POST"])
def adminsignup():
    return singup_controller()

@admin.route('/logout',methods=["POST"])
def adminlogout():
    session.pop("admin")
    return {"Message":"Logout"}
