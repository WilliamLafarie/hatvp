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

df15 = pd.read_sql_table('hatvp_exercices', engine)
df_15 = df15.rename(columns={'exercices_id': 'ID de l\'exercice', 'annee_debut': 'Année de début', 'annee_fin': 'Année de fin', 'ca_inf': 'Chiffre d\'affaire inférieur', 'ca_sup': 'Chiffre d\'affaire supérieur', 'chiffre_affaires': 'Chiffre d\'affaire', 'date_debut': 'Date de début', 'date_fin': 'Date de fin', 'date_publication': 'Date de publication', 'declaration_incomplete': 'Déclaration incomplète', 'exercice_sans_CA': 'Exercice sans chiffre d\'affaire', 'exercice_sans_activite': 'Exercice sans activité', 'montant_depense': 'Montant de la dépense', 'montant_depense_inf': 'Montant de dépense inférieur', 'montant_depense_sup': 'Montant de dépense supérieur', 'nombre_activite': 'Nombre d\'activité', 'nombre_salaries': 'Nombre de salariés', 'representants_id_id': 'ID du représentant'})

# Page size for the dash table
PAGE_SIZE = 20

app = DjangoDash('Exercices')

app.layout = html.Div([
    html.Div([
        dash_table.DataTable(
            id='table-for-informations',
            columns=[{'name': i, 'id': i, 'deletable': True} for i in df_15.columns],
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
        dff_1 = df_15.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff_1 = df_15
    return dff_1.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')