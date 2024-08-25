from flask import Blueprint

third = Blueprint('third', __name__)

@third.route('/child2/')
def index2():

    return 'flask框架-third Blue'
