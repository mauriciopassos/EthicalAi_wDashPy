import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, name="14th Dilemma", title="Ethical Dilemmas in Software Development")

d14Title = html.Section(
            [
                html.H2("14th Dilemma"),
            ]
)

progress = dbc.Progress(value=(15/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > You were hired to enhance the appointment scheduling software for a medical clinic. **During the development process, you learn that the personal data collected is encrypted by an insecure hash (SHA1). You can enhance the system by changing the hash used to a more robust version (SHA 256)**. However, **this does not change the fact that the personal data of this clinic's clients was relatively unprotected during the time the system was being used**. Improving the encryption protocol used will require a development and testing period equivalent to (approximately) 1 month. **During this time, this clinic's data will be vulnerable**.
        ''')

d14 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-14-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Advises that those in charge of the clinic notify their clients, and temporarily remove their application from the air.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Proposes that the upgrade of the encryption protocol (SHA1 to SHA 256) be done during the next month, without this being disclosed to the clinic's clients.", "value": 3},
                ],
                value=2,
                id="dilemma-14-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d14Img = html.Img(src='assets/img/dilemma_14.gif', alt="Animation of a paper icon with many numbers changing on it.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   #href=dash.page_registry['pages.d14']['relative_path'],
                   href="#",
                   id='go-to-14', n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d14Title,
            mdown,
            d14,
            d14Img,
            btn
        ]
)

