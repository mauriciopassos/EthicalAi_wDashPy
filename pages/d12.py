import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from pages import d13

dash.register_page(__name__, name="12th Dilemma", title="Ethical Dilemmas in Software Development")

d12Title = html.Section(
            [
                html.H2("12th Dilemma"),
            ]
)

progress = dbc.Progress(value=(13/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > Machine learning models perform tasks for which they are trained. **When developing an autonomous learning system, an inaccuracy was noticed resulting in discrimination involving a group representing 6.2% of the population where the model will be applied**. However, the system has already **been approved by the CEO and COO of the company** due to the good performance results obtained.
        ''')

d12 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-12-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Evidence a lack of accuracy in presenting the model on its own.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Since the decision making is not yours, you deliver the model as approved.", "value": 3},
                ],
                value=2,
                id="dilemma-12-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d12Img = html.Img(src='assets/img/dilemma_12.gif', alt="Animation of various people with the caption 'Protect all LGBTQ workers'.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   href=dash.page_registry['pages.d13']['relative_path'],
                   id='go-to-12', n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d12Title,
            mdown,
            d12,
            d12Img,
            btn
        ]
)

