import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from pages import d09

dash.register_page(__name__, name="8th Dilemma", title="Ethical Dilemmas in Software Development")

d08Title = html.Section(
            [
                html.H2("8th Dilemma"),
            ]
)

progress = dbc.Progress(value=(9/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > You have been the point of contact within your company for all projects related to a specific client. One day, **you receive a message in your personal email from that client requesting your services to be paid as a contractor on a project completely unrelated to all the previous work they have requested with the company**.
        ''')

d08 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-8-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Accept the client's work.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Notify your manager about the request.", "value": 3},
                ],
                value=2,
                id="dilemma-8-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d08Img = html.Img(src='assets/img/dilemma_8.gif', alt="Animation of a business man wearing sunglasses saying 'Come work with me'.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   href=dash.page_registry['pages.d09']['relative_path'],
                   id='go-to-8', n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d08Title,
            mdown,
            d08,
            d08Img,
            btn
        ]
)