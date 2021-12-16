from flask import Blueprint
from flask import render_template 

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')


@views.route('/main')
def main():
    return "<h1>MAIN</h1>"