# ==========================================
# Components
# ==========================================

from dash import html, dcc
import dash_bootstrap_components as dbc

from theme import (
    CARD,
    TEXT,
    BACKGROUND
)

def create_kpi_card(title, value, color):

    return dbc.Card(

        dbc.CardBody(

            [

                html.H6(

                    title,

                    style={

                        "color": "#CBD5E1",

                        "fontWeight": "600",

                        "marginBottom": "8px"

                    }

                ),

                html.H2(

                    value,

                    style={

                        "color": color,

                        "fontWeight": "bold",

                        "margin": 0

                    }

                )

            ]

        ),

        style={

            "backgroundColor": CARD,

            "border": "none",

            "borderRadius": "18px",

            "padding": "10px",

            "boxShadow": "0px 4px 15px rgba(0,0,0,0.25)"

        }

    )

def create_header():

    return html.Div(

        [

            html.H1(

                "Retail Customer Analytics Dashboard",

                style={

                    "textAlign": "center",

                    "color": TEXT,

                    "fontWeight": "bold",

                    "fontSize": "40px"

                }

            ),

            html.P(

                "RFM Based Customer Segmentation",

                style={

                    "textAlign": "center",

                    "color": "#94A3B8",

                    "fontSize": "18px"

                }

            ),

            html.Hr(

                style={

                    "borderColor": "#334155"

                }

            )

        ]

    )

def create_filter_panel(df):

    return dbc.Card(

        dbc.CardBody(

            [

                dbc.Row(

                    [

                        dbc.Col(

                            dcc.Dropdown(

                                id="segment_filter",

                                options=[

                                    {

                                        "label": "All",

                                        "value": "All"

                                    }

                                ] +

                                [

                                    {

                                        "label": i,

                                        "value": i

                                    }

                                    for i in sorted(

                                        df["Segment"].unique()

                                    )

                                ],

                                value="All",

                                clearable=False

                            ),

                            width=4

                        ),

                        dbc.Col(

                            dcc.Dropdown(

                                id="rscore_filter",

                                options=[

                                    {

                                        "label":"All",

                                        "value":"All"

                                    }

                                ] +

                                [

                                    {

                                        "label":str(i),

                                        "value":i

                                    }

                                    for i in range(1,6)

                                ],

                                value="All",

                                clearable=False

                            ),

                            width=4

                        ),

                        dbc.Col(

                            html.Div(

                                "Filters",

                                style={

                                    "color":TEXT,

                                    "fontWeight":"bold",

                                    "fontSize":"20px",

                                    "textAlign":"center",

                                    "paddingTop":"6px"

                                }

                            ),

                            width=4

                        )

                    ]

                )

            ]

        ),

        style={

            "backgroundColor": CARD,

            "border":"none",

            "borderRadius":"18px"

        }

    )

def create_section_title(title):

    return html.H3(

        title,

        style={

            "color": TEXT,

            "fontWeight": "bold",

            "marginTop": "25px",

            "marginBottom": "15px"

        }

    )