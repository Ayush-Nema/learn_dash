"""
Simple application
=====================
It contains the codebase to create a basic application with the dropdown menu.
Source link: https://towardsdatascience.com/dash-for-beginners-create-interactive-python-dashboards-338bfcb6ffa4

# to list the content running in the port 8050
$ lsof -i :8050

# to kill the activity running in the port
$ kill <PID>
"""

import dash
from dash import html
import plotly.graph_objects as go
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash()

df = px.data.stocks()

app.layout = html.Div(id='parent', children=[
    html.H1(id='H1', children='Styling using html components', style={'textAlign': 'center',
                                                                      'marginTop': 40, 'marginBottom': 40}),

    dcc.Dropdown(id='dropdown',
                 options=[
                     {'label': 'Google', 'value': 'GOOG'},
                     {'label': 'Apple', 'value': 'AAPL'},
                     {'label': 'Amazon', 'value': 'AMZN'},
                 ],
                 value='GOOG'),
    dcc.Graph(id='bar_plot')
])


@app.callback(Output(component_id='bar_plot', component_property='figure'),
              [Input(component_id='dropdown', component_property='value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = go.Figure([go.Scatter(x=df['date'], y=df['{}'.format(dropdown_value)],
                                line=dict(color='firebrick', width=4))
                     ])

    fig.update_layout(title='Stock prices over time',
                      xaxis_title='Dates',
                      yaxis_title='Prices'
                      )
    return fig


if __name__ == '__main__':
    app.run_server()
