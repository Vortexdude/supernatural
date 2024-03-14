import falcon.asgi
from superbot.routes.main import add_routes


def create_app():
    """Main entrypoint of the app"""

    app = falcon.asgi.App()
    add_routes(app)

    return app
