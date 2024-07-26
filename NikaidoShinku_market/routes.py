from flask import Blueprint, render_template

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def home():
    return render_template('index.html')

@routes_bp.route('/login')
def login():
    return render_template('login.html')