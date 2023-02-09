import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from pages import ssc

dash.register_page(__name__, name="16th Dilemma", title="Ethical Dilemmas in Software Development")

d16Title = html.Section(
            [
                html.H2("16th Dilemma"),
            ]
)

progress = dbc.Progress(value=(17/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > Your company has taken on the project of developing a software application that **delivers an image classification service whose data leakage could pose a very high degree of risk to the lives of employees**. This is a strategic contract for the company at this time. **During the briefing phase, the client shows concern with the security level of the solution**.
        ''')

d16 = dbc.Row(
    [
        dbc.Label("Even knowing that it could represent a significant budget increase and the risk of losing the contract, what do you do?", html_for="dilemma-16-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Included in the solution development is the hiring of a company to perform attacks on the solution, in order to identify vulnerabilities.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Given that the firing of a pen testing agent would make the service more expensive, you don't suggest this solution.", "value": 3},
                ],
                value=2,
                id="dilemma-16-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d16Img = html.Img(src='assets/img/dilemma_16.gif', alt="Animation of a scene in Jurassic Park (the movie from 1993) where Samuel L. Jackson speaks 'I Hate this hacker crap' while looking at a computer screen.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   href=dash.page_registry['pages.ssc']['relative_path'],
                   id='go-to-16', n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d16Title,
            mdown,
            d16,
            d16Img,
            btn
        ]
)

