from flask import Flask,redirect,url_for
from routes.products import products
from routes.admin import admin
from dotenv import load_dotenv
import os

load_dotenv()

app=Flask(__name__) 
app.register_blueprint(products)
app.register_blueprint(admin)
app.secret_key=os.getenv("SECRET_KEY")

@app.route('/')
def root():
    return redirect(url_for('admin.adminlogin'))

def get_app():
    return app
