from flask import Flask

from App.views import init_view

from App.views.second_blue import second


def creat_app():

    app = Flask(__name__)

    # app.register_blueprint(blue)
    #
    # app.register_blueprint(second)

    init_view(app=app)

    return app
