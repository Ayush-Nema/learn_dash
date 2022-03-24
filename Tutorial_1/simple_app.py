"""
Sample script for Dash-based app
==================================
- Source: https://towardsdatascience.com/dash-for-beginners-create-interactive-python-dashboards-338bfcb6ffa4
"""

import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import plotly.express as px

# Initialising dash app
app = dash.Dash()

# Reading stock price dataset
df = px.data.stocks()


def stock_prices():
    # function for creating line chart showing Google stock price over time
    fig = go.Figure([
        go.Scatter(x=df['date'], y=df['GOOG'],
                   line=dict(color='firebrick', width=4), name='Google')
    ])

    fig.update_layout(title='Prices over time',
                      xaxis_title='Dates',
                      yaxis_title='Prices')
    return fig


app.layout = html.Div(id='parent', children=[
    html.H1(id='H1', children='Styling over html components', style={'textAlign': 'center',
                                                                     'marginTop': 40,
                                                                     'marginBottom': 40}),
    dcc.Graph(id='line_plot', figure=stock_prices())
])

if __name__ == '__main__':
    app.run_server()
