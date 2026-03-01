from flask import session
from functools import wraps

def is_login(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if "admin" not in session:
            return {"Message" : "Not Loged In"},401
        return f(*args,**kwargs)
    return wrapper