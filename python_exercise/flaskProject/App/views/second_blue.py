from flask import Blueprint

second = Blueprint('second', __name__)

@second.route('/child1/')
def index1():

    return 'flask框架-second Blue'