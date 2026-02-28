from flask import Blueprint

admin=Blueprint("admin",__name__,url_prefix="/admin")

@admin.route('/login',methods=["GET","POST"])
def adminlogin():
    return "Welcom Admin"


@admin.route('/signup',methods=["GET","POST"])
def adminsignup():
    return "New Admin Added"
