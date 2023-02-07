import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, name="1st Dilemma", title="Ethical Dilemmas in Software Development")

d01Title = html.Section(
            [
                html.H2("1st Dilemma"),
            ]
)

progress = dbc.Progress(value=(2/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > The manufacturing department has developed a new technology to enable a specific feature that users have been requesting for a long time. Unfortunately, the technology cannot operate without causing the electromagnetic fields from cell phone towers to increase beyond legal limits. While this feature has not been possible for the past few years, if you wait until you can approach the legal limits, competitors will likely beat you to the market. **One manager suggests changing the software on the devices to detect when the regulatory tests are happening and modify their behavior to prevent the electromagnetic field from increasing**.
        ''')

d01 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-1-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Begin development of the test detection software.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Wait until the technology is available, without test detection software, and risk being beaten to market.", "value": 3},
                ],
                value=2,
                id="dilemma-1-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d01Img = html.Img(src='assets/img/dilemma_1.gif', alt="Animation of a TV screen having signal problems.",
                        style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-bottom': '15px', 'width': '43%'}
                    )


btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   #href=dash.page_registry['pages.d02']['relative_path'],
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
            d01Title,
            mdown,
            d01,
            d01Img,
            btn
        ]
)

