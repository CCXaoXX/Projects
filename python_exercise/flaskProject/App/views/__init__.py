from .first_blue import blue

from .second_blue import second

from .third_blue import third


def init_view(app):
    app.register_blueprint(blue)
    app.register_blueprint(second)
    app.register_blueprint(third)