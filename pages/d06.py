import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from pages import d07

dash.register_page(__name__, name="6th Dilemma", title="Ethical Dilemmas in Software Development")

d06Title = html.Section(
            [
                html.H2("6th Dilemma"),
            ]
)

progress = dbc.Progress(value=(7/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > While reviewing a software specification that your company has just been contracted to create, **your team discovers a major flaw that could potentially affect the customer**. Your company has spent the last year trying to negotiate this lucrative contract. **Your managers do not want to tell the customer about it because it could further prolong the negotiations**.
        ''')

d06 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-6-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Informs the customer about the issue.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Does not tell the client about the issue. ", "value": 3},
                ],
                value=2,
                id="dilemma-6-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d06Img = html.Img(src='assets/img/dilemma_6.gif', alt="Animation of Peter Griffin (main character in the series Family Guy)laying down naked with the caption 'You Can Trust Us'.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   href=dash.page_registry['pages.d07']['relative_path'],
                   id='go-to-6',  n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d06Title,
            mdown,
            d06,
            d06Img,
            btn
        ]
)

