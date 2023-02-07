import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, name="Demographic Information", title="Ethical Dilemmas in Software Development")

demographicTitle = html.Section(
            [
              html.H2("Demographic Information"),
            ]
)

progress = dbc.Progress(value=(1/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})


email_input = dbc.Row(
    [
        dbc.Label("Email", html_for="email-row", width=2),
        dbc.Col([
            dbc.Input(id="email-input-c", type="email",
                      value="example@example.com", required=True),
            dbc.FormText("Type in a valid email...")
        ], width=10,
        ),
    ],
    className="mb-3",
)

age_input = dbc.Row(
    [
        dbc.Label("Age", html_for="age-row", width=2),
        dbc.Col([
            dbc.Input(value=18, id="age-input-c",
                      type="number", min=18, max=100, step=1, required=True),
            dbc.FormText(
                "Type in your age (you have to be over 18 to participate in this research)..."),
        ], width=10,
        ),
    ],
    className="mb-3",
)

status_input = dbc.Row(
    [
        dbc.Label("Developer Status", html_for="status-row", width=2),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Student", "value": 1},
                    {"label": "Intern", "value": 2},
                    {"label": "Junior Developer", "value": 3},
                    {"label": "Mid-Level Developer", "value": 4},
                    {"label": "Senior  Developer", "value": 5},
                ],
                value=1,
                id="status-input-c",
            ),
            dbc.FormText(
                "What is your current status in Software Development..."),
        ],
            width=10,
        ),
    ],
    className="mb-3",
)


formation_input = dbc.Row(
    [
        dbc.Label("Formation in IT", html_for="formation-row", width=2),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Computer Science", "value": 1},
                    {"label": "Software Engineering", "value": 2},
                    {"label": "Information Systems", "value": 3},
                    {"label": "Computer Engineering", "value": 4},
                    {"label": "Self Taught", "value": 5},
                    {"label": "Other", "value": 6},
                ],
                value=1,
                id="formation-input-c",
            ),
            dbc.FormText(
                "Choose the formation that best describes your formation..."),
        ],
            width=10,
        ),
    ],
    className="mb-3",
)

gender_input = dbc.Row(
    [
        dbc.Label("Gender", html_for="gender-row", width=2),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Male", "value": 1},
                    {"label": "Female", "value": 2},
                    {"label": "Non-Binary", "value": 3},
                    {"label": "Other", "value": 4},
                ],
                value=3,
                id="gender-input-c",
            ),
            dbc.FormText(
                "Choose the gender option that best describes your identity..."),
        ],
            width=10,
        ),
    ],
    className="mb-3",
)

demo_form = dbc.Form([
    email_input,
    age_input,
    status_input,
    formation_input,
    gender_input
], style={'margin-top': '30px'}
)


# for page in dash.page_registry.values():
#     print(page)
#     print("\n")

btn = html.A("Next >>", className="button", href="#")

layout = dbc.Container(
      [
        progress,
        demographicTitle,
        demo_form,
        btn
      ]
)

