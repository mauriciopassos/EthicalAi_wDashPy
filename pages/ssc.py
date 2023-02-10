import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, callback, State

dash.register_page(__name__, name="Self-assessment - Santa Clara Ethics Scale", title="Ethical Dilemmas in Software Development")

progress = dbc.Progress(value=(18/18) * 100, color="#1a66d1",
                        className="mb-3", animated=True, striped=True,
                        style={"height": "10px", "width": "100%"})

mdown = dcc.Markdown('''
        ## Self-assessment (Santa Clara Ethics Scale)

        **Congratulations! You have had to make difficult decisions. Now that the quiz is closed, we would like you to answer the following two last questions:**
        ''')


self_1 = dbc.Row(
    [
        dbc.Label("How would you describe your ethical training in dealing with situations of the kind experienced in the dilemmas you have just dealt with in your academic/professional training?",
                  html_for="self-1-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Insufficient.", "value": 1},
                    {"label": "I received some guidance.", "value": 2},
                    {"label": "Cases like these were mentioned and discussed in my professional/academic training.", "value": 3},
                    {"label": "I received sufficient instruction to deal with all the situations listed in this study.", "value": 4},
                    {"label": "Nothing to state.", "value": 5},

                ],
                value=3,
                id="self-1-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

self_2 = dbc.Row(
    [
        dbc.Label("Regarding the following statement: 'Ethical guidelines have a necessary importance in the practice of professions related to the field of Information and Technology', you:",
                  html_for="self-2-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "Strongly agree.", "value": 1},
                    {"label": "Agree.", "value": 2},
                    {"label": "Nothing to state.", "value": 3},
                    {"label": "Disagree.", "value": 4},
                    {"label": "I strongly disagree.", "value": 5},

                ],
                value=3,
                id="self-2-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

secondmdown = dcc.Markdown('''
        **Now, please answer the following questions using the scale below. Indicate the level of agreement (or disagreement) for each statement:**
        ''')

santa_clara_1 = dbc.Row(
    [
        dbc.Label("Respecting others, even those who I don't like or agree with, is very important to me.",
                  html_for="self-2-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "I strongly disagree.", "value": 1},
                    {"label": "Disagree.", "value": 2},
                    {"label": "Agree.", "value": 3},
                    {"label": "I strongly agree.", "value": 4},

                ],
                value=3,
                id="santa-clara-1-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

santa_clara_2 = dbc.Row(
    [
        dbc.Label("Being responsible and accountable, even when I have to admit that I’m wrong or have errored, is very important to me.",
                  html_for="self-2-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "I strongly disagree.", "value": 1},
                    {"label": "Disagree.", "value": 2},
                    {"label": "Agree.", "value": 3},
                    {"label": "I strongly agree.", "value": 4},

                ],
                value=3,
                id="santa-clara-2-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

santa_clara_3 = dbc.Row(
    [
        dbc.Label("Being honest, fair, and maintaining integrity, even when it might put me at a disadvantage, is very important to me.",
                  html_for="self-2-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "I strongly disagree.", "value": 1},
                    {"label": "Disagree.", "value": 2},
                    {"label": "Agree.", "value": 3},
                    {"label": "I strongly agree.", "value": 4},

                ],
                value=3,
                id="santa-clara-3-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

santa_clara_4 = dbc.Row(
    [
        dbc.Label("I strive to be competent in my areas of personal or professional expertise and am the first to admit it when I am not and have fallen short.",
                  html_for="self-2-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "I strongly disagree.", "value": 1},
                    {"label": "Disagree.", "value": 2},
                    {"label": "Agree.", "value": 3},
                    {"label": "I strongly agree.", "value": 4},

                ],
                value=3,
                id="santa-clara-4-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

santa_clara_5 = dbc.Row(
    [
        dbc.Label("I feel a great deal of compassion for others, even those whom I don’t know or have few things in common with.",
                  html_for="self-2-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "I strongly disagree.", "value": 1},
                    {"label": "Disagree.", "value": 2},
                    {"label": "Agree.", "value": 3},
                    {"label": "I strongly agree.", "value": 4},

                ],
                value=3,
                id="santa-clara-5-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

santa_clara_6 = dbc.Row(
    [
        dbc.Label("I have clear ethical guiding principles that I keep in mind and follow at all times.",
                  html_for="self-2-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "I strongly disagree.", "value": 1},
                    {"label": "Disagree.", "value": 2},
                    {"label": "Agree.", "value": 3},
                    {"label": "I strongly agree.", "value": 4},

                ],
                value=3,
                id="santa-clara-6-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

santa_clara_7 = dbc.Row(
    [
        dbc.Label("It is more important for me to behave ethically than to get an advantage in life.",
                  html_for="self-2-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "I strongly disagree.", "value": 1},
                    {"label": "Disagree.", "value": 2},
                    {"label": "Agree.", "value": 3},
                    {"label": "I strongly agree.", "value": 4},

                ],
                value=3,
                id="santa-clara-7-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

santa_clara_8 = dbc.Row(
    [
        dbc.Label("I never take advantage of others and am truthful in my relationships and interactions even when it might put me at a disadvantage.",
                  html_for="self-2-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "I strongly disagree.", "value": 1},
                    {"label": "Disagree.", "value": 2},
                    {"label": "Agree.", "value": 3},
                    {"label": "I strongly agree.", "value": 4},

                ],
                value=3,
                id="santa-clara-8-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

santa_clara_9 = dbc.Row(
    [
        dbc.Label("I would not be embarrassed if all of my actions were filmed and played back for others to see and evaluate.",
                  html_for="self-2-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "I strongly disagree.", "value": 1},
                    {"label": "Disagree.", "value": 2},
                    {"label": "Agree.", "value": 3},
                    {"label": "I strongly agree.", "value": 4},

                ],
                value=3,
                id="santa-clara-9-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

santa_clara_10 = dbc.Row(
    [
        dbc.Label("I typically ask myself what the right thing to do is from an ethical or moral perspective before making decisions.",
                  html_for="self-2-row", width=4),
        dbc.Col([
            dbc.RadioItems(
                options=[
                    {"label": "I strongly disagree.", "value": 1},
                    {"label": "Disagree.", "value": 2},
                    {"label": "Agree.", "value": 3},
                    {"label": "I strongly agree.", "value": 4},

                ],
                value=3,
                id="santa-clara-10-input",
            ),
        ],
            width=8,
        ),
    ],
    className="mb-5",
)

submit_button = html.Div(
    [
        dbc.Button(["Submit", html.I(className="bi bi-chevron-double-right")],
                  color="light", outline=False, size="xl",
                  id='submit-button', n_clicks=0,
                  className="mt-3 mb-3",
                  ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)

thank_you = dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(
                    "The End! 🤗"), close_button=False),
                dbc.ModalBody(
                    dcc.Markdown('''
                    Thank you very much for being part of our survey! 

                    This research was made possible by the effort of two organizations: the [AI Robotics Ethics Society](https://en.airespucrs.org/) (**AIRES**) at PUC-RS, and the [Network for Ethical and Safe Artificial Intelligence](https://www.raies.org/en) (**RAIES**).

                    At the AI Robotics Ethics Society, **we focus on educating tomorrow's AI leaders in ethical AI principles to ensure AI is created ethically and responsibly**.

                    The Network for Ethical and Safe Artificial Intelligence emerged at the intersection of researchers, companies, universities, and national and international institutions, to promote the development of safe and ethical Artificial Intelligence. In a world **where technology advances rapidly, playing an increasingly central role in our lives, it is vital that ethical precepts, along with safety mechanisms, advance in the same proportion - and this is our task**.

                    If you would like to learn more about the research we are conducting within AIRES and RAIES, please visit this [link](https://nkluge-correa.github.io/on-going.html)!
                    ''')
                ),
                dbc.ModalFooter(
                    dbc.Button(
                        "Have a nice day! 👋", n_clicks=0, color="light", outline=False, href="/"
                    )
                ),
            ],
            keyboard=False,
            backdrop="static",
            id="thank-you",
            size="lg",
            is_open=False,
        )

layout = dbc.Container(
        [
            progress,

            mdown,
            self_1,
            self_2,
            html.Hr(),

            secondmdown,
            santa_clara_1,
            santa_clara_2,
            santa_clara_3,
            santa_clara_4,
            santa_clara_5,
            santa_clara_6,
            santa_clara_7,
            santa_clara_8,
            santa_clara_9,
            santa_clara_10,
            
            thank_you,
            submit_button,
        ]
)

# @callback(
#     Output('thank-you', 'is_open'),
#     Input('submit-button', 'n_clicks'),
#     State('thank-you', 'is_open'),
# )
# def toggle_submit(n_clicks, is_open):
#     if n_clicks > 0:
#         return not is_open
#     return is_open