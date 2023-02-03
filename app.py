import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__,
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}],
                    external_stylesheets=['https://fonts.googleapis.com/css2?family=Share+Tech&display=swap',dbc.themes.BOOTSTRAP],
                    use_pages=True)

app.title = "Ethical Dilemmas in Software Development"

title = html.H1("Ethical Dilemmas in Software Development")
header = html.Header(title)

app.layout = dbc.Container(
    [
        header,

        dash.page_container
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=1237)