import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, name="7th Dilemma", title="Ethical Dilemmas in Software Development")

d07Title = html.Section(
            [
                html.H2("7th Dilemma"),
            ]
)

progress = dbc.Progress(value=(8/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > You are on a team tasked with maintaining critical software for a customer's financial system. **During testing, you discover a critical bug that has been present for a long time.** While you fix it, **your manager does not want to inform the customer** for fear that he might doubt your company's competence.
        ''')

d07 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-7-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Inform the customer about the bug.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Don't tell the customer about the bug.", "value": 3},
                ],
                value=2,
                id="dilemma-7-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d07Img = html.Img(src='assets/img/dilemma_7.gif', alt="A black and white animation of someone trying to clear a train track while in front of a moving train.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   #href=dash.page_registry['pages.d08']['relative_path'],
                   href="#",
                   id='go-to-7', n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d07Title,
            mdown,
            d07,
            d07Img,
            btn
        ]
)

