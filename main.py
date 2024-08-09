from dash import Dash, html, Input, Output, dcc
from dash_bootstrap_components.themes import BOOTSTRAP
from src.pages import home
from src.components import navbar


def main():
    app = Dash(external_stylesheets=[BOOTSTRAP], title="Image Super resolution")

    app.layout = html.Div(
        className="app-div",
        children=[
            dcc.Location(id='url', refresh=False),
            html.H1(app.title,className="text-center text-primary"),
            navbar.render(),
            html.Div(id="page-content")
        ]
    )

    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/':
            return home.create_layout(app)

    app.run(debug=True, port="8080")


if __name__ == '__main__':
    main()