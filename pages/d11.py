import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, name="11th Dilemma", title="Ethical Dilemmas in Software Development")

d11Title = html.Section(
            [
                html.H2("11th Dilemma"),
            ]
)

progress = dbc.Progress(value=(12/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > As you are leaving your office for an **extremely important** project with a potential new client, you hear the administrative assistant say, "_If John calls, please see that he calls home, his spouse says there is a mini-crisis_". You are to meet John at the client's office, and the two of **you are to make a presentation** (_pitch_). **John's participation is crucial**. John is quite nervous and often gives a bad impression if distracted.
        ''')

d11 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-11-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Tell John about the situation before the meeting.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Not tell John about the situation before the meeting.", "value": 3},
                ],
                value=2,
                id="dilemma-11-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d11Img = html.Img(src='assets/img/dilemma_11.gif', alt="Animation of a scientist pointing to a globe of the Earth catching fire saying 'This is an actual crisis'.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   #href=dash.page_registry['pages.d12']['relative_path'],
                   href="#",
                   id='go-to-11', n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d11Title,
            mdown,
            d11,
            d11Img,
            btn
        ]
)

