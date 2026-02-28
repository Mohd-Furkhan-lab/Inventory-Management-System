from flask import Flask
from routes.products import products
from routes.admin import admin

app=Flask(__name__)
app.register_blueprint(products)
app.register_blueprint(admin)
app.secret_key="Mfasdfasdf"


def get_app():
    return app