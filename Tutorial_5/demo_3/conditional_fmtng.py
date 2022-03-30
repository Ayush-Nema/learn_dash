"""
App demonstrating Conditional Formatting in `Datatables`
=========================================================\
Video link: https://www.youtube.com/watch?v=S8ZcErBpfYE
Source code: https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/DataTable/Conditional_Formatting

Reference link2:
- https://dash.plotly.com/datatable/conditional-formatting
- https://dash.plotly.com/datatable/reference
"""
import dash
from dash import html, dcc
import plotly.express as px
from dash import dash_table
from dash.dependencies import Input, Output
from table_bars import data_bars
import pandas as pd

df = pd.read_csv("data/medical supplies.csv")
df["Part sent date"] = pd.to_datetime(df["Part sent date"]).dt.date
df["Part received date"] = pd.to_datetime(df["Part received date"]).dt.date
df["Prioritise"] = df["Machines"].apply(lambda x:
                                        '★★★' if x > 3000 else (
                                            '★★' if x > 1000 else (
                                                '★' if x > 500 else '')))

# Initialise the application
app = dash.Dash(__name__)
