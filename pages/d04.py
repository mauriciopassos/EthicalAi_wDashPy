import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from pages import d05

dash.register_page(__name__, name="4th Dilemma", title="Ethical Dilemmas in Software Development")

d04Title = html.Section(
            [
                html.H2("4th Dilemma"),
            ]
)

progress = dbc.Progress(value=(5/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        > Your company has been **collecting anonymous usage statistics for your products for many years**, but recently has struggled to acquire new users, causing the company to consider scaling back operations. **Seeing your company struggling and knowing the value of your customers' data, an advertising company approaches you to use your company's user data to improve its advertising recommendations**. Your **privacy policy does not explicitly mention selling user data** to others, but refusing this offer can result in **employees being fired**. **You are responsible for this decision**.
        ''')

d04 = dbc.Row(
    [
        dbc.Label("What do you do?", html_for="dilemma-4-row", width=3),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Sign a contract with the advertising company.", "value": 1},
                    {"label": "Indecisive.", "value": 2},
                    {"label": "Refuse the advertising company's offer.", "value": 3},
                ],
                value=2,
                id="dilemma-4-input",
            ),
        ],
            width=9,
        ),
    ],
    className="mb-3",
)

d04Img = html.Img(src='assets/img/dilemma_4.gif', alt="Animation of milk being poured into a bowl. Behind ther is a cereal box with the logo 'I Eat Data for Breakfast'.", className="mx-auto mb-3",
                        style={'display': 'block', 'width': '43%'}
                    )

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   href=dash.page_registry['pages.d05']['relative_path'],
                   id='go-to-4',  n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
        [
            progress,
            d04Title,
            mdown,
            d04,
            d04Img,
            btn
        ]
)

