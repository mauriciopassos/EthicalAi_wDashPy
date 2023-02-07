import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from pages import scenario

dash.register_page(__name__, name="ACM", title="Ethical Dilemmas in Software Development")

ACMTitle = html.Section(
            [
              html.H2("ACM Code of Ethics and Professional Conduct"),
              html.P("Assista o vídeo a seguir e clique em Concordar...")
            ]
)

viFrame = html.Iframe(
              width="700", height="394",
#              src="https://www.youtube.com/embed/4iHgNAc6HlU",
              src="https://www.youtube.com/embed/OI-G23HF6Sw",
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

btn = html.A("I confirm that I have read the ACM Code of Ethics", className="button", href=dash.page_registry['pages.scenario']['relative_path'])

# for page in dash.page_registry.values():
#     print(page)
#     print("\n")

layout = dbc.Container(
      [
        ACMTitle,
        videoFrame,
        linklearnMore,
        sectionlearnMore,
        btn
      ]
)

