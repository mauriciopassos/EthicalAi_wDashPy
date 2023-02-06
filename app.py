import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__,
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}],
                    external_stylesheets=['https://fonts.googleapis.com/css2?family=Share+Tech&display=swap',dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP],
                    use_pages=True)

app.title = "Ethical Dilemmas in Software Development"

title = html.H1("Ethical Dilemmas in Software Development")
header = html.Header(title)

badges = html.Div(
            [
                dbc.Badge([html.I(className="bi bi-bank"), "  AIRES at PUCRS"], href="https://en.airespucrs.org/",
                    className="text-decoration-none"),
                dbc.Badge([html.I(className="bi bi-filetype-py"), "  Made with Python"], href="https://www.python.org/",
                    className="text-decoration-none"),
                dbc.Badge([html.I(className="bi bi-github"), "  Nkluge-correa"], href="https://nkluge-correa.github.io/",
                    className="text-decoration-none")
            ]
)

footer = html.Section(badges, className="fbagdes")

app.layout = dbc.Container(
    [
        header,

        dash.page_container,

        footer
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=1237)