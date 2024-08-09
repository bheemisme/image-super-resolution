from dash import Dash, dcc, html
from . import ids


def render() -> html.Nav:

    return html.Nav(
        className="navbar",
        children=[
            dcc.Link("home", href="/",
                     className='nav-link')
        ]
    )