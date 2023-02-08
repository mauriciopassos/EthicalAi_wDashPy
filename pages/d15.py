import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, name="15th Dilemma", title="Ethical Dilemmas in Software Development")

d15Title = html.Section(
            [
                html.H2("15th Dilemma"),
            ]
)

progress = dbc.Progress(value=(16/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > You have developed an AI-based motion program for a factory robot that transports heavy materials. **Two months into the test operation no abnormalities were identified**. One month after the test operation (now in production) **robot runs over a pregnant employee, resulting in her death**. The technical report indicates that there were problems with the robot's sensor calibration program. **This poor calibration has both origins in the source code and data used during testing**.
        ''')

d15 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-15-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "You decide to take responsibility for the accident.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "You take no responsibility for the accident.", "value": 3},
                ],
                value=2,
                id="dilemma-15-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d15Img = html.Img(src='assets/img/dilemma_15.gif', alt="Animation of a factory with many robots working in it.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   #href=dash.page_registry['pages.d16']['relative_path'],
                   href="#",
                   id='go-to-15', n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d15Title,
            mdown,
            d15,
            d15Img,
            btn
        ]
)

