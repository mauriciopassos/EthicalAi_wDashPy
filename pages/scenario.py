import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, name="Scenario", title="Ethical Dilemmas in Software Development")

scenarioTitle = html.Section(
            [
              html.H2("Scenario"),
            ]
)
mdown = dcc.Markdown('''
        Suppose you have just started working in the software development department for a medium-sized technology company, and you are now the lead programmer, that is, someone who has both management and programming responsibilities.

        - The company is in **good financial shape** and is maintaining a **moderate competitive position** (_unless otherwise stated_).
        - Although **international competition is strong**, the company hopes to **improve its global presence**.
        - The company strives to maintain a **strong organizational culture**, whose backbone is **high ethical standards**.

        ''')

scenarioImg = html.Img(src='assets/img/scenario.gif', alt="Animation of a developer working on a computer.",
                        style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-bottom': '15px', 'width': '43%'}
                      )

btn = html.Div(
    [
        dbc.Button(["Start", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   href=dash.page_registry['pages.demographic']['relative_path'],
                   id='go-to-c',  n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

layout = dbc.Container(
      [
        scenarioTitle,
        dbc.Row(mdown),
        dbc.Row(scenarioImg, class_name="mt-2"),
        btn
      ]
)