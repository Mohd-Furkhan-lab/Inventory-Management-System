from db.admin_model import login_check,admin_signup
import bcrypt
from flask import session

def admin_login_check(data):
    if data:
        name=data.get("name")
        password=data.get("password")
        store_password=login_check(name)
        if store_password:
            res=bcrypt.checkpw(password.encode('utf-8'),store_password)
            if res:
                session["admin"]=name
                return True
            else:
                return None
    return None         
        
def add_admin(data):
    if data:
        adid=data.get("id")
        name=data.get("name")
        password=data.get("password")
        pswd_bytes=password.encode('utf-8')
        hashed=bcrypt.hashpw(pswd_bytes,bcrypt.gensalt())
        res=admin_signup(adid,name,hashed)
        if res:
            return True
        else:
            return None
    else:
        return None