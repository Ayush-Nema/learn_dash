"""
Tutorial on creating a dash app
=================================
Data source: https://www.kaggle.com/datasets/neuromusic/avocado-prices
Article source link: https://realpython.com/python-dash/
"""
import dash
from dash import dcc
from dash import html
import pandas as pd

data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)
print(data.columns)

# Initialising the dash app
app = dash.Dash(name=__name__)

app.layout = html.Div(
    children=[
        html.H1(
            children="Avocado Analytics",
            style={"fontSize": "48px", "color": "red"},
        ),
        html.P(
            children="Analyze the behavior of avocado prices"
                     " and the number of avocados sold in the US between 2015 and 2018",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
