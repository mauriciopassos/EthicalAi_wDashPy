import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, callback, State

from pages import d01

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
            dbc.Input(id="email-input-c", type="email", value="example@example.com", required=True),
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
            dbc.Input(value=18, id="age-input-c", type="number", min=18, max=100, step=1, required=True),
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
], className="mt-4",
)

# for page in dash.page_registry.values():
#     print(page)
#     print("\n")

btn = html.Div(
    [
        dbc.Button(["Next", html.I(className="bi bi-chevron-double-right")],
                   color="light", outline=False, size="xl",
                   href=dash.page_registry['pages.d01']['relative_path'],
                   id='go-to-c',  n_clicks=0,
                   className="mt-3 mb-3",
                   ),
    ],
    className="d-grid gap-2 col-6 mx-auto",
)



offcanvas = html.Div(
    [
        html.Div(
            [
                dbc.Button(
                    "Privacy Policy", id='open-offcanvas-c', outline=False, color='light', n_clicks=0, className='ms-auto',
                ),
            ], className="d-grid gap-2 col-12 mx-auto",
        ),
        dbc.Offcanvas(
            [
                dcc.Markdown('''
                    At _AIRES_, privacy and security are priorities and we are committed to transparency in the handling of personal data of our subjects. Therefore, this Privacy Policy sets out how we collect, use and transfer information from the subjects of this research.

                    By participating in this survey, you understand that we will collect and use your personal information in the ways described in this Policy, under the rules of the Federal Constitution of 1988 (art. 5, LXXIX; and art. 22, XXX - included by EC 115/2022), of the Data Protection rules (LGPD, Federal Law 13.709/2018), of the consumerism provisions of Federal Law 8078/1990 and the other applicable rules of the Brazilian legal system.

                    Accordingly, the _AI Robotics Ethics Society_, hereinafter referred to simply as "AIRES", registered in the role of Data Controller, is bound by the provisions of this Privacy Policy.

                    ##### What data do we collect about you and for what purpose?

                    Our site collects and uses some personal data about you (_only those filled in the form below_), in order to enable our research objectives.

                    ##### Personal Data Provided by the Holder

                    -   _Email so that we can contact the volunteer after the end of our survey. This way we can share our results with all those who participated. If you do not want this contact, just use the email already filled in the form._
                    -   _Age, Education, Professional Status and Gender are collected so that we can make a comparison of the results discretizing the demographic variables mentioned above._
                    - _The answers of the dilemmas are used so that we can evaluate the behavior of software developers in situations of moral uncertainty._

                    ##### Automatically Collected Personal Data

                    -   _No personal data is collected automatically_.

                    ##### How do we collect your data?

                    In this sense, the collection of your personal data takes place as follows:

                    -   _All data collected is done by the form after submission. no data is collected before the volunteer submits the form._

                    ##### Consent

                    It is based on your consent that we process your personal data. Consent is the free, informed and unambiguous expression by which you authorize _AIRES_ to process your data.

                    Thus, in line with the General Data Protection Act, your data will only be collected, processed and stored upon prior and express consent.

                    Your consent will be obtained in a specific manner for each purpose described above, evidencing the commitment of transparency and good faith of _AIRES_ to its volunteers, following the relevant legislative regulations.

                    By participating in this survey and providing your personal data, you are aware of and consenting to the provisions of this Privacy Policy, as well as knowing your rights and how to exercise them.

                    At any time and at no cost, you may revoke your consent.

                    It is important to point out that the revocation of consent for the treatment of data may imply the impossibility of the adequate performance of some functionality of the site that depends on the operation. Such consequences will be informed in advance.

                    ##### What are your rights?

                    _AIRES_ assures its users/customers of their rights as provided for in article 18 of the General Data Protection Law. Thus, you may, free of charge and at any time:

                    - **Confirm the existence of data processing**, in a simplified manner or in a clear and complete format.
                    - **Access your data**, which you can request in a legible hard copy or by electronic, secure and reliable means.
                    - **Correct your data**, by requesting to edit, correct or update them.
                    - **To limit your data** when it is unnecessary, excessive or treated in violation of the law by anonymization, blocking or deletion.
                    - **Request the portability of your data**, through a report that _AIRES_ treats about you.
                    - **To delete your data** processed with your consent, except in cases provided for by law.
                    - **Withdraw your consent** to the processing of your data.
                    - **To inform yourself of the possibility of not giving your consent** and the consequences of refusing to do so.

                    ##### How can you exercise your rights as a holder?

                    To exercise your rights as a holder, you should contact _AIRES_ through the following available means:

                    - [airespucrs@airespucrs.org](mailto:airespucrs@airespucrs.org).
                    - [raies@raies.org](mailto:raies@raies.org).

                    ##### How and for how long will your data be stored?

                    Your personal data collected by _AIRES_ will be used and stored for as long as necessary for the completion of the "_Ethical Dilemmas in Software Development_" research.

                    In general, your data will be kept for as long as it is necessary for our survey to be completed. After completion and publication of our results, all your personal data will be deleted from our database.

                    The storage of data collected by _AIRES_ reflects our commitment to the security and privacy of your data. We employ technical protection measures and solutions that guarantee the confidentiality, integrity and inviolability of your data. In addition, we also have security measures that are appropriate to the risks and control access to the information stored.

                    ##### What do we do to keep your data secure?

                    To keep your personal information secure, we use physical, electronic, and managerial tools geared to protecting your privacy.

                    We apply these tools taking into consideration the nature of the personal data collected, the context and purpose of the processing, and the risks that potential breaches would create to the rights and freedoms of the data subject of the data collected and processed.

                    Among the measures we adopt, we highlight the following:

                    - Only authorized persons have access to your personal data
                    - Access to your personal data is made only after a confidentiality commitment
                    - Your personal data is stored in a secure and suitable environment.

                    _AIRES_ is committed to adopting the best postures to avoid security incidents. However, it is necessary to point out that no web site is entirely safe and risk free. It is possible that, despite all our security protocols, problems that are exclusively the fault of third parties may occur, such as cyber attacks by _hackers_.

                    In case of security incidents that may generate relevant risk or damage to you or any of our users/customers, we will notify those affected and the National Data Protection Authority about the occurrence, in line with the provisions of the General Data Protection Law.

                    ##### Who can your data be shared with?

                    In order to preserve your privacy, _AIRES_ will not share your personal data with any third party.

                    Your data may be shared only with the researchers involved in this research.

                    They receive your data only to the extent necessary. Our researchers are guided by the data protection regulations of the Brazilian legal system.

                    ##### Cookies or Navigation Data

                    The _AIRES_ **does not use Cookies on this research tool**.

                    ##### Changes to this Privacy Policy

                    The current version of the Privacy Policy was last formulated and updated on:  _(21/11/2022)_.

                    ##### Liability

                    _AIRES_ provides for the liability of the agents involved in the data processing processes, in accordance with articles 42 to 45 of the General Data Protection Law.

                    We are committed to keeping this Privacy Policy up to date, observing its provisions and ensuring its fulfillment.

                    In addition, we also undertake to seek technical and organizational conditions that are certainly able to protect the entire data processing process.

                    Should the Data Protection Authority require that steps be taken in relation to the data processing carried out by _AIRES,_ we undertake to follow them.

                    ##### Disclaimer

                    As mentioned in Topic 6, although we adopt high security standards in order to avoid incidents, no virtual site is entirely free of risks. In this sense, _AIRES_ is not responsible for:

                    I - Any consequences arising from the negligence, imprudence or malpractice of users in relation to their individual data. We guarantee and are only responsible for the security of the data treatment processes and the fulfillment of the purposes described in this instrument.

                    II - Malicious actions of third parties, such as attacks by _hackers_, except in case of proven culpable or deliberate conduct by _AIRES._ We highlight that in case of security incidents that may generate relevant risk or damage to you or any of our users/customers, we will inform the affected parties and the National Data Protection Authority about the occurrence and we will take the necessary measures.

                    ##### Data Protection Officer

                    _AIRES_ provides the following means for you to contact us to exercise your rights as a data subject:  

                    - [airespucrs@airespucrs.org](mailto:airespucrs@airespucrs.org).
                    - [raies@raies.org](mailto:raies@raies.org).

                    If you have any questions about this Privacy Policy or the personal data we process, you may contact our Personal Data Protection Officer through the following channels:

                    _Nicholas Kluge Corrêa_.
                    [nicholas@airespucrs.org](mailto:airespucrs@airespucrs.org).
                    
                    
                    '''),
            ],
            id="offcanvas-c",
            scrollable=True,
            title="Privacy Policy",
            placement='end',
            is_open=False,
            style={'width': '70vw'}
        ),
    ]
)



layout = dbc.Container(
        [
            progress,
            demographicTitle,
            html.Div(offcanvas),
            demo_form,
            btn
        ]
)


@callback(
    Output("offcanvas-c", "is_open"),
    Input("open-offcanvas-c", "n_clicks"),
    State("offcanvas-c", "is_open"),
)
def toggle_offcanvas_scrollable(n1, is_open):
    if n1:
        return not is_open
    return is_open