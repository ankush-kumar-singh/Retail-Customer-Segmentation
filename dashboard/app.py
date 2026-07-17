# ==========================================
# Dash Application
# ==========================================

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


# Components
from components import (
    create_header,
    create_kpi_card,
    create_filter_panel,
    create_section_title
)


# Data
from data import (
    df,
    total_customers,
    total_revenue,
    avg_monetary,
    champions
)


# Theme
from theme import (
    BACKGROUND,
    PRIMARY,
    SUCCESS,
    WARNING
)


# ==========================================
# Initialize App
# ==========================================

app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.DARKLY
    ]
)

server = app.server
# ==========================================
# Dashboard Layout
# ==========================================

app.layout = html.Div(

    [

        create_header(),


        # KPI Section
        dbc.Row(

            [

                dbc.Col(

                    html.Div(
                        id="total_customers_card",
                        children=create_kpi_card(
                            "Total Customers",
                            f"{total_customers:,}",
                            PRIMARY
                        )
                    ),

                    width=3

                ),


                dbc.Col(

                    html.Div(
                        id="total_revenue_card",
                        children=create_kpi_card(
                            "Total Revenue",
                            f"₹ {total_revenue:,.0f}",
                            SUCCESS
                        )
                    ),

                    width=3

                ),


                dbc.Col(

                    html.Div(
                        id="avg_value_card",
                        children=create_kpi_card(
                            "Average Customer Value",
                            f"₹ {avg_monetary:,.2f}",
                            WARNING
                        )
                    ),

                    width=3

                ),


                dbc.Col(

                    html.Div(
                        id="champions_card",
                        children=create_kpi_card(
                            "Champions",
                            f"{champions:,}",
                            PRIMARY
                        )
                    ),

                    width=3

                )

            ],

            className="mb-4"

        ),



        # Filters

        create_filter_panel(df),



        # Segment Analysis

        create_section_title(
            "Customer Segment Analysis"
        ),


        dbc.Row(

            [

                dbc.Col(

                    dcc.Graph(
                        id="segment_bar_chart"
                    ),

                    width=6

                ),


                dbc.Col(

                    dcc.Graph(
                        id="segment_donut_chart"
                    ),

                    width=6

                )

            ]

        ),



        # RFM Analysis

        create_section_title(
            "RFM Customer Behaviour"
        ),


        dbc.Row(

            [

                dbc.Col(

                    dcc.Graph(
                        id="bubble_chart"
                    ),

                    width=12

                )

            ]

        ),



        # Customer Value

        create_section_title(
            "Customer Value Analysis"
        ),


        dbc.Row(

            [

                dbc.Col(

                    dcc.Graph(
                        id="boxplot_chart"
                    ),

                    width=6

                ),


                dbc.Col(

                    dcc.Graph(
                        id="top_customers_chart"
                    ),

                    width=6

                )

            ]

        ),



        # Correlation

        create_section_title(
            "RFM Correlation"
        ),


        dbc.Row(

            [

                dbc.Col(

                    dcc.Graph(
                        id="heatmap_chart"
                    ),

                    width=12

                )

            ]

        )

    ],


    style={

        "backgroundColor": BACKGROUND,

        "minHeight": "100vh",

        "padding": "30px"

    }

)



# Register Callbacks

from callbacks import register_callbacks

register_callbacks(app)



# ==========================================
# Run Server
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )