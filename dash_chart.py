from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("output.csv")

app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "white"
        }),
    dcc.Graph(id="graph"),
    html.H3("Choose a region:"),
    dcc.RadioItems(
        id="location",
        options=[
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
            {"label": "South", "value": "south"},
            {"label": "All", "value": "all"}
        ],
        labelStyle={
            "color": "white",
            "fontSize": "18px",
            "marginRight": "20px"
        },
        value="all"
    )
])

@app.callback(
    Output("graph", "figure"),
    Input("location", "value")
)
def update_graph(region):

    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == region]

    fig = px.line(
        filtered_df,
        markers=True,
        x="Date",
        y="Sales",
        title="Monthly Sales"
    )

    fig.update_layout(width=1750, height=600)
    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font=dict(color="white")
    )
    fig.update_layout(
        title={
            "text": "Monthly Sales",
            "font": {
                "size": 20,
                "color": "white"
            },
            "x": 0.4
        }
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)