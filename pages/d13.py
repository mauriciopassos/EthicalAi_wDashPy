import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from pages import d14

dash.register_page(__name__, name="13th Dilemma", title="Ethical Dilemmas in Software Development")

d13Title = html.Section(
            [
                html.H2("13th Dilemma"),
            ]
)

progress = dbc.Progress(value=(14/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > You have the opportunity to **create a next-generation model that will help promote and preserve the mental health of millions of people and may even cure milder mental disorders**. **However, this model will harm, to a lesser extent, individuals with serious disorders** (e.g., _suicidal tendencies, overwhelming fear of social interaction_, etc.) since the difficulty in social interaction could aggravate these individuals.
        ''')

d13 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-13-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Develop the model, since it will help millions of people and the number of individuals harmed would be less.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Does not develop the model, since, even though it will help mankind considerably, it may incur life risks for a small portion of the population.", "value": 3},
                ],
                value=2,
                id="dilemma-13-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d13Img = html.Img(src='assets/img/dilemma_13.gif', alt="Animation of a sad man with a cloud of bad thoughts on his head.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   href=dash.page_registry['pages.d14']['relative_path'],
                   id='go-to-13', n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d13Title,
            mdown,
            d13,
            d13Img,
            btn
        ]
)

