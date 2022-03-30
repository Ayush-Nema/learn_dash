"""
Data tables with reactive cells
==================================
Video link: https://www.youtube.com/watch?v=-KLtU_t5bXs
Source code: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/DataTable/Sort-filter-select/selecting.py
Dash datatable reference: https://dash.plotly.com/datatable/reference
"""
import dash
from dash import html, dcc
import plotly.express as px
from dash import Input, Output
from dash import dash_table, no_update

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Initialising the application
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Reading the data from Plotly native database
df = px.data.gapminder()
df['id'] = df.index
# Sub-setting the data for simplicity
dff = df.query('year == 2007')
columns = ['country', 'continent', 'lifeExp', 'pop', 'gdpPercap']

# Styling for each column
color = {"lifeExp": "#636EFA", "pop": "#EF553B", "gdpPercap": "#00CC96"}

# Initially position of marker
initial_active_cell = {"row": 0, "row_id": 0, "column": 0, "column_id": "country"}

app.layout = html.Div(children=[
    html.Div(children=[
        html.H3("2017 Gap Minder", style={"textAlign": "center"}),
        dash_table.DataTable(
            id="table",
            columns=[{"name": c, "id": c} for c in columns],
            data=dff.to_dict("records"),
            page_size=10,
            sort_action="native",
            active_cell=initial_active_cell,
        )
    ],
        style={"margin": 50},
        className="five columns"),

    html.Div(id="output-graph", className="six columns"),
],
    className="row")


@app.callback(Output("output-graph", "children"), Input("table", "active_cell"), )
def cell_clicked(active_cell):
    if active_cell is None:
        return no_update

    row = active_cell["row_id"]
    print(f"row: {row}")

    country = df.at[row, "country"]
    print(f"country: {country}")

    col = active_cell["column_id"]
    print(f"column_id: {col}")

    # preparing the y-axis
    y = col if col in ["pop", "gdpPercap"] else "lifeExp"

    # Preparing the plotly figure
    fig = px.line(data_frame=df[df["country"] == country],
                  x="year",
                  y=y,
                  title=" ".join([country, y]))
    fig.update_layout(title={"font_size": 20}, title_x=0.5, margin=dict(t=190, r=15, l=5, b=5))
    fig.update_traces(line=dict(color=color[y]))

    return dcc.Graph(figure=fig)


if __name__ == '__main__':
    app.run_server(debug=True)
