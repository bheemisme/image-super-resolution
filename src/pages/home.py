from dash import Dash, html


def create_layout(app: Dash) -> html.Div:
    
    layout = html.Div(
        className="home-div",
        children=[
            html.Div(className="body-container px-sm py-md", children=[
                html.Div(className="chart-container d-flex flex-md-row align-items-center flex-wrap flex-column",
                         children=[
                            
                             
                         ])
            ])
        ],
    )

    return layout