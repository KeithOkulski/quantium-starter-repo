
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv("output.csv")
# Create line chart

fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Monthly Sales",
    markers=True
)
fig.update_layout(
    width=7000,
    height=600
)


# Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)