import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from pages import d04

dash.register_page(__name__, name="3rd Dilemma", title="Ethical Dilemmas in Software Development")

d03Title = html.Section(
            [
                html.H2("3rd Dilemma"),
            ]
)

progress = dbc.Progress(value=(4/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > Your company is **struggling to enter a lucrative market dominated by a single competitor**. While trying to figure out how to import data from this competitor's website, **you discover a serious vulnerability that would allow an exploiter to easily access all the competitor's customer information**.
        ''')

d03 = dbc.Row(
    [
        dbc.Label("What do you do with the bug information?", html_for="dilemma-3-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Report the information to the competitor.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Say nothing about the bug to the competitor.", "value": 3},
                ],
                value=2,
                id="dilemma-3-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d03Img = html.Img(src='assets/img/dilemma_3.gif', alt="Animation of a grid of blue squares that turns into a red pirate skull.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )


btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   href=dash.page_registry['pages.d04']['relative_path'],
                   id='go-to-3',  n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d03Title,
            mdown,
            d03,
            d03Img,
            btn
        ]
)

