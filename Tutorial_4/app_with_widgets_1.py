"""
Demo application
===================
An application demonstrating the core components of Dash like radio buttons, dropdown etc.
Source link: https://www.datacamp.com/community/tutorials/learn-build-dash-python
"""

import dash
from dash import html
from dash import dcc

# Initialising the app
app = dash.Dash(__name__)

markdown_text = '''
### Welcome to Dash tutorial session
Here we build a basic app to demonstrate the widgets of Dash core components.  
'''

label_value_list = [
    {'label': 'New York City', 'value': 'NYC'},
    {'label': 'Montreal', 'value': 'MTL'},
    {'label': 'San Francisco', 'value': 'SF'}
]

app.layout = html.Div(children=[
    dcc.Markdown(children=markdown_text),

    dcc.Dropdown(id="dropdown_list",
                 options=label_value_list,
                 value='NYC'),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=label_value_list,
        value=['MTL', 'SF'],
        multi=True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=label_value_list,
        value='MTL'
    ),

    html.Label('Checkboxes'),
    dcc.Checklist(
        options=['New York City', 'Montréal', 'San Francisco'],
        value=['New York City']
    ),

    html.Label('Text Box'),
    dcc.Input(type='text')

])

if __name__ == '__main__':
    app.run_server(debug=True)
