# ==========================================
# Charts
# ==========================================

import plotly.express as px
import plotly.graph_objects as go

from theme import (
    BACKGROUND,
    CARD,
    TEXT,
    GRID,
    SEGMENT_COLORS
)

# ==========================================
# Common Layout
# ==========================================

def apply_layout(fig, title):

    fig.update_layout(

        title={
            "text": title,
            "x": 0.5,
            "font": {
                "size": 22,
                "color": TEXT
            }
        },

        paper_bgcolor=CARD,
        plot_bgcolor=CARD,

        font={
            "color": TEXT,
            "family": "Segoe UI"
        },

        margin=dict(
            l=30,
            r=30,
            t=60,
            b=30
        ),

        xaxis=dict(
            showgrid=False,
            zeroline=False
        ),

        yaxis=dict(
            gridcolor=GRID,
            zeroline=False
        ),

        legend=dict(
            bgcolor=CARD
        )

    )

    return fig

# ==========================================
# Segment Distribution
# ==========================================

def create_segment_bar(segment_counts):

    fig = px.bar(

        segment_counts,

        x="Segment",

        y="Customers",

        color="Segment",

        text="Customers",

        color_discrete_map=SEGMENT_COLORS

    )

    fig.update_traces(

        textposition="outside"

    )

    fig = apply_layout(

        fig,

        "Customer Distribution by Segment"

    )

    return fig

# ==========================================
# Segment Share Donut Chart
# ==========================================

def create_segment_donut(segment_counts):

    fig = px.pie(

        segment_counts,

        names="Segment",

        values="Customers",

        hole=0.60,

        color="Segment",

        color_discrete_map=SEGMENT_COLORS

    )

    fig.update_traces(

        textposition="inside",

        textinfo="percent+label",

        pull=[0.03]*len(segment_counts)

    )

    fig = apply_layout(

        fig,

        "Customer Segment Share"

    )

    return fig

# ==========================================
# RFM Bubble Chart
# ==========================================

def create_bubble_chart(df):

    fig = px.scatter(

        df,

        x="Recency",

        y="Frequency",

        size="Monetary",

        color="Segment",

        hover_name="Customer ID",

        size_max=60,

        opacity=0.75,

        color_discrete_map=SEGMENT_COLORS

    )

    fig = apply_layout(

        fig,

        "RFM Customer Bubble Analysis"

    )

    fig.update_xaxes(title="Recency")

    fig.update_yaxes(title="Frequency")

    return fig

# ==========================================
# Monetary Distribution
# ==========================================

def create_boxplot(df):

    fig = px.box(

        df,

        x="Segment",

        y="Monetary",

        color="Segment",

        color_discrete_map=SEGMENT_COLORS,

        points="outliers"

    )

    fig = apply_layout(

        fig,

        "Monetary Distribution by Segment"

    )

    return fig

# ==========================================
# Top Customers
# ==========================================

def create_top_customers(df):

    top = (

        df

        .sort_values(

            "Monetary",

            ascending=False

        )

        .head(20)

    )

    fig = px.bar(

        top,

        x="Customer ID",

        y="Monetary",

        color="Monetary",

        color_continuous_scale="Viridis",

        text="Monetary"

    )

    fig = apply_layout(

        fig,

        "Top 20 Customers"

    )

    return fig

# ==========================================
# Correlation Heatmap
# ==========================================

def create_heatmap(df):

    corr = df[

        [

            "Recency",

            "Frequency",

            "Monetary"

        ]

    ].corr()

    fig = go.Figure(

        data=go.Heatmap(

            z=corr.values,

            x=corr.columns,

            y=corr.columns,

            colorscale="Viridis",

            text=corr.round(2),

            texttemplate="%{text}"

        )

    )

    fig = apply_layout(

        fig,

        "RFM Correlation Matrix"

    )

    return fig

