from flask import Blueprint

blue = Blueprint('Blue', __name__)

@blue.route('/')
def index():

    return 'flask框架--blue-print'