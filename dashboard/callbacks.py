print("CALLBACK FILE LOADED")


from dash import Input, Output


from charts import (
    create_segment_bar,
    create_segment_donut,
    create_bubble_chart,
    create_boxplot,
    create_top_customers,
    create_heatmap
)


from components import create_kpi_card


from theme import (
    PRIMARY,
    SUCCESS,
    WARNING
)


from data import df



def register_callbacks(app):


    @app.callback(

        [

            Output("total_customers_card","children"),

            Output("total_revenue_card","children"),

            Output("avg_value_card","children"),

            Output("champions_card","children"),


            Output("segment_bar_chart","figure"),

            Output("segment_donut_chart","figure"),

            Output("bubble_chart","figure"),

            Output("boxplot_chart","figure"),

            Output("top_customers_chart","figure"),

            Output("heatmap_chart","figure")

        ],


        [

            Input("segment_filter","value"),

            Input("rscore_filter","value")

        ]

    )


    def update_dashboard(segment, rscore):


        print("CALLBACK RUNNING")

        print("Segment:", segment)

        print("R Score:", rscore)



        filtered_df = df.copy()



        if segment != "All":

            filtered_df = filtered_df[

                filtered_df["Segment"] == segment

            ]



        if rscore != "All":

            filtered_df = filtered_df[

                filtered_df["R_score"] == rscore

            ]



        segment_counts = (

            filtered_df["Segment"]

            .value_counts()

            .reset_index()

        )


        segment_counts.columns = [

            "Segment",

            "Customers"

        ]



        return (


            create_kpi_card(

                "Total Customers",

                f"{len(filtered_df):,}",

                PRIMARY

            ),



            create_kpi_card(

                "Total Revenue",

                f"₹ {filtered_df['Monetary'].sum():,.0f}",

                SUCCESS

            ),



            create_kpi_card(

                "Average Customer Value",

                f"₹ {filtered_df['Monetary'].mean():,.2f}",

                WARNING

            ),



            create_kpi_card(

                "Champions",

                f"{(filtered_df['Segment']=='Champions').sum():,}",

                PRIMARY

            ),



            create_segment_bar(segment_counts),

            create_segment_donut(segment_counts),

            create_bubble_chart(filtered_df),

            create_boxplot(filtered_df),

            create_top_customers(filtered_df),

            create_heatmap(filtered_df)

        )