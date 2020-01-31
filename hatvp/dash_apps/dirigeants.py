import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
from django_plotly_dash import DjangoDash
import pandas as pd
from sqlalchemy import create_engine
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASS"),
        'HOST': 'localhost',
        # 'PORT': '',
    }
}

# choose the database to use
db = DATABASES['default']

# construct an engine connection string
engine_string = "postgresql+psycopg2://{user}:{password}@{host}/{database}".format(
    user=db['USER'],
    password=db['PASSWORD'],
    host=db['HOST'],
    # port = db['PORT'],
    database=db['NAME'],
)

# create sqlalchemy engine
engine = create_engine(engine_string)

df2 = pd.read_sql_table('hatvp_dirigeants', engine)
df_2 = df2.rename(columns={'id': 'ID', 'civilite_dirigeant': 'Civilité du dirigeant', 'fonction_dirigeant': 'Fonction du dirigeant', 'nom_dirigeant': 'Nom du dirigeant', 'nom_prenom_dirigeant': 'Nom et prénom du dirigeant', 'prenom_dirigeant': 'Prénom du dirigeant', 'representants_id_id': 'ID du représentant'})

# Page size for the dash table
PAGE_SIZE = 20

app = DjangoDash('Dirigeants')

app.layout = html.Div([
    html.Div([
        dash_table.DataTable(
            id='table-for-informations',
            columns=[{'name': i, 'id': i, 'deletable': True} for i in df_2.columns],
            page_current=0,
            page_size=PAGE_SIZE,
            page_action='custom',

            sort_action='custom',
            sort_mode='single',
            sort_by=[]
        )
    ]),
])

# Code pour le tableau
@app.callback(
    Output('table-for-informations', 'data'),
    [
        Input('table-for-informations', "page_current"),
        Input('table-for-informations', "page_size"),
        Input('table-for-informations', 'sort_by')
    ])
def update_table(page_current, page_size, sort_by):
    if len(sort_by):
        dff_1 = df_2.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff_1 = df_2
    return dff_1.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')