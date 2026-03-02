from flask import session,redirect,url_for
from functools import wraps

def is_login(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.adminlogin"))
        return f(*args,**kwargs)
    return wrapper