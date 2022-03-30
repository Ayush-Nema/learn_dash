"""
Table with click-callback
============================
source link: https://dash.plotly.com/datatable
"""

import dash
from dash import Input, Output, callback
from dash import dash_table
import dash_bootstrap_components as dbc
import pandas as pd

# reading the data
df = pd.read_csv('https://git.io/Juf1t')

# Initialising the application
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Getting the layout
app.layout = dbc.Container([
    dbc.Label("Click a cell in the table"),
    dash_table.DataTable(df.to_dict('records'), id='tbl'),
    dbc.Alert(id='tbl_out')
])


@callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table!"


if __name__ == '__main__':
    app.run_server(debug=True)
