import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path="/", name="Consent", title="Ethical Dilemmas in Software Development")

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

videoFrame = html.Section(viFrame, className="videoFrame")

linklearnMore = html.A(
                "> Saiba mais...",
                href="#",
                className="lLM",
)

sectionlearnMore = html.Section(
                [
                  html.P("Este espaço é destinado as informações do Saiba Mais...")
                ],
                className="learnMore hide"
)

btn = html.Div(
    [
          dbc.Button(
                'I agree to participate in the this research',
                id='close-consent',
                className='ms-auto',
                n_clicks=0,
                color='light',
                outline=True
                )
    ],
    className="d-grid gap-2 d-md-flex justify-content-md-end",
)

layout = dbc.Container(
      [
        consentTitle,
        videoFrame,
        linklearnMore,
        sectionlearnMore,
        btn
      ]
)

