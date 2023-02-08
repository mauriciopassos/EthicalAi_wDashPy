import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from pages import d11

dash.register_page(__name__, name="10th Dilemma", title="Ethical Dilemmas in Software Development")

d10Title = html.Section(
            [
                html.H2("10th Dilemma"),
            ]
)

progress = dbc.Progress(value=(11/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > The company is currently being **sued by a customer who claims to have been injured by one of the company's products**. In your development tasks, you discover a piece of your company's open-sourced code that has not been analyzed for years. **You find a way to affect the customer's personal injury claim**. There is a large sum of money at stake and the company is currently in good shape to win the case.
        ''')

d10 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-10-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Disclose the information to the customer.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Not revealing the information to the customer.", "value": 3},
                ],
                value=2,
                id="dilemma-10-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d10Img = html.Img(src='assets/img/dilemma_10.gif', alt="Animation of a judge (a 'The Simpsons' character) hitting her gavel with the caption 'CASE DISMISSED'.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   href=dash.page_registry['pages.d11']['relative_path'],
                   id='go-to-10', n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d10Title,
            mdown,
            d10,
            d10Img,
            btn
        ]
)

