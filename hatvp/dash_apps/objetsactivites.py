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

df8 = pd.read_sql_table('hatvp_objets_activites', engine)
df_8 = df8.rename(columns={'activite_id': 'ID de l\'activité', 'date_publication_activite': 'Date de la publication de l\'activité', 'exercices_id_id': 'ID de l\'exercice', 'identifiant_fiche': 'ID de la fiche', 'objet_activite': 'Object de l\'activité'})

# Page size for the dash table
PAGE_SIZE = 20

app = DjangoDash('ObjetsActivites')

app.layout = html.Div([
    html.Div([
        dash_table.DataTable(
            id='table-for-informations',
            columns=[{'name': i, 'id': i, 'deletable': True} for i in df_8.columns],
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
        dff_1 = df_8.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff_1 = df_8
    return dff_1.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')