import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from pages import d10

dash.register_page(__name__, name="9th Dilemma", title="Ethical Dilemmas in Software Development")

d09Title = html.Section(
            [
                html.H2("9th Dilemma"),
            ]
)

progress = dbc.Progress(value=(10/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > Rumor has it that your former employer is the lead for a new software product that could be an industry breakthrough. **On the morning of the beginning of your third week in your current job, you receive the following memo from the president**: _Please meet me tomorrow at 8:15 to discuss the developments that your former employer has made in this new area_.
        ''')

d09 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-9-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Tell the president that you will not discuss the matter.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Meet with the president knowing the purpose of the discussion.", "value": 3},
                ],
                value=2,
                id="dilemma-9-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d09Img = html.Img(src='assets/img/dilemma_9.gif', alt="Animation of Julius Cesar with multiple knives in his back, showing the caption 'Who Could You?'.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   href=dash.page_registry['pages.d10']['relative_path'],
                   id='go-to-9', n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d09Title,
            mdown,
            d09,
            d09Img,
            btn
        ]
)

