import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px
import gunicorn
import os

# Creating a bar chart using Dash to display the monthly expenditure data
df = pd.read_csv('new_file.csv')
df = df.sort_values(by="ITEM CATEGORY")

app = dash.Dash(__name__)
server = app.server

figure = px.bar(df, x=["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE"], y="ITEM CATEGORY", title="My Expenses")

app.layout = html.Div(children=[
    html.H1(children='Monthly Expenditure'),

    dcc.Graph(
        id='my-expenses-chart',
        figure=figure
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)
