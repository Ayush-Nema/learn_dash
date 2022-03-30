"""
App with data table
=====================
A demonstration of basic application with Dash's data table.
Source link: https://dash.plotly.com/datatable
"""

from dash import Dash, dash_table
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
print(df.head())
app = Dash(__name__)

app.layout = dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])

if __name__ == '__main__':
    app.run_server(debug=True)
