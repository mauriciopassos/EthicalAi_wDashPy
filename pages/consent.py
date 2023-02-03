import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path="/", name="BlaConsent", title="Ethical Dilemmas in Software Development")

consentTitle = html.Section(
            [
              html.H2("Online Study Consent Form"),
              html.P("Assista o vídeo a seguir e clique em Concordar...")
            ]
)

viFrame = html.Iframe(
              width="700", height="394",
              src="https://www.youtube.com/embed/P5HNeahRYDM",
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; fullscreen" ,
              )

videoFrame = html.Div(viFrame, className="videoFrame")

saibaMais = html.P("> Saiba mais...")


layout = dbc.Container(
      [
        consentTitle,
        videoFrame,
        saibaMais,
      ]
)