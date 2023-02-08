import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from pages import d02

dash.register_page(__name__, name="1st Dilemma", title="Ethical Dilemmas in Software Development")

d02Title = html.Section(
            [
                html.H2("2nd Dilemma"),
            ]
)

progress = dbc.Progress(value=(3/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > A deadline is **fast approaching for a project you are working on**. You realize that you will not be able to meet the deadline if you work only during normal hours. **You are not allowed to take your computer out of the office**.
        ''')

d02 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-2-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Download the data onto a personal hard drive so you can continue development at home.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Stay at work longer in order to continue development.", "value": 3},
                ],
                value=2,
                id="dilemma-2-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d02Img = html.Img(src='assets/img/dilemma_2.gif', alt="Animation of a developer working on a computer (very attentive) with code lines passing on the background.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )


btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   #href=dash.page_registry['pages.d03']['relative_path'],
                   href="#",
                   id='go-to-c',  n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d02Title,
            mdown,
            d02,
            d02Img,
            btn
        ]
)

