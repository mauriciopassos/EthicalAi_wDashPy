import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, name="Scenario", title="Ethical Dilemmas in Software Development")

consentTitle = html.Section(
            [
              html.H2("Scenario"),
            ]
)


# for page in dash.page_registry.values():
#     print(page)
#     print("\n")

btn = html.A("Start", className="button", href="#")

layout = dbc.Container(
      [
        consentTitle,

        btn
      ]
)

