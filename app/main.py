from flask import Flask
from app.routes.products import products
from app.routes.admin import admin


app=Flask(__name__) 
app.register_blueprint(products)
app.register_blueprint(admin)
app.secret_key="Mfasdfasdf"


def get_app():
    return app
