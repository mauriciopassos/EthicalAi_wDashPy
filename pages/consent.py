import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

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
              [
                html.I(className="learnarrow bi bi-arrow-right-short"),
                " Saiba mais..."
              ],
                href="#",
                className="lLM",
)

sectionlearnMore = html.Section(
                [
                  #html.P("Este espaço é destinado as informações do Saiba Mais...")
                  dcc.Markdown(
                    """
                    Este espaço é _destinado as informações_ do **Saiba Mais**...
                    """
                  )
                ],
                className="learnMore hide"
)

# btn = html.Div(
#     [
#           dbc.Button(
#                 'I agree to participate in the this research',
#                 id='close-consent',
#                 className='ms-auto',
#                 n_clicks=0,
#                 color='light',
#                 outline=True
#                 )
#     ],
#     className="d-grid gap-2 d-md-flex justify-content-md-end",
# )

#btn = html.A("I agree to participate in the this research", className="button", href=dash.page_registry['pages.acm']['relative_path'])


btn = html.Div(
    [
      dbc.Button('I agree to participate in the this research',
                  id='close-consent',
                  className='ms-auto',
                  n_clicks=0,
                  color='light',
                  outline=False,
                  size="xl",
                  href=dash.page_registry['pages.acm']['relative_path']
                )
    ], className="mt-3 d-grid gap-2 col-12 mx-auto",
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

