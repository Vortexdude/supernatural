from falcon import asgi
from superbot.utils.status import Status, CType
import falcon


class CustomClass:
    async def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = Status.HTTP_200  # This is the default status
        resp.content_type = CType.MEDIA_TEXT  # Default is JSON, so override
        resp.text = (
            '\nTwo things awe me most, the starry sky '
            'above me and the moral law within me.\n'
            '\n'
            '    ~ Immanuel Kant\n\n'
        )


da = CustomClass()


def add_routes(app: asgi.App()) -> None:
    app.add_route('/hello_world', da)
