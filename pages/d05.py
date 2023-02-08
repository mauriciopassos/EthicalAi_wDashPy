import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, name="5th Dilemma", title="Ethical Dilemmas in Software Development")

d05Title = html.Section(
            [
                html.H2("5th Dilemma"),
            ]
)

progress = dbc.Progress(value=(6/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > To protect against unauthorized use of your software, your company has incorporated an automatic shutdown switch that prevents it from running after a specific period. **An intensive care unit at the local hospital started using your software a year ago**. The unit has not paid any of its bills, and the shutoff switch is about to trigger. **If the kill switch remains in place, the hospital will not be able to function because critical equipment will be disabled**. You can remove the switch for the hospital.
        ''')

d05 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-5-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Edit the software to remove the off switch.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Do nothing, allowing the switch to remain operative.", "value": 3},
                ],
                value=2,
                id="dilemma-5-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d05Img = html.Img(src='assets/img/dilemma_5.gif', alt="Animation of an electrocardiogram with a signal of a beating heart.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   #href=dash.page_registry['pages.d06']['relative_path'],
                   href="#",
                   id='go-to-5',  n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d05Title,
            mdown,
            d05,
            d05Img,
            btn
        ]
)

