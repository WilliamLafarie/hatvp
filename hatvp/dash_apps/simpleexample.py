import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
from django_plotly_dash import DjangoDash


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Nombre de lignes du tableau
PAGE_SIZE = 20

app = DjangoDash('SimpleExample')

app.layout = html.Div([
    dcc.Markdown('''
    #### HATVP Project

    Travail réalisé par **[William Lafarie](https://www.linkedin.com/in/william-lafarie/?originalSubdomain=fr)**, **[Odom Ear](https://www.linkedin.com/in/odom-ear/)**, **[Sébastien Cosneau](https://www.linkedin.com/in/sébastien-cosneau-56b72a104/)** et **[Gauthier Magne](https://www.linkedin.com/in/gauthier-magne-7a0805127/)**

    Ce projet a été réalisé dans le cadre du cours de Python dispensé par **[Anthony Baillard](https://www.linkedin.com/in/anthonybaillard/?originalSubdomain=fr)** à **[Hétic](https://www.hetic.net)**
    ''',
                 style={
                     'textAlign': 'center',
                     'color': 'red',
                     'fontSize': 24,
                     'fontFamily': 'open-sans',
                     'fontWeight': 'normal',
                     'fontVariant': 'small-caps',
                     'textDecoration': 'underline'
                 }),

])