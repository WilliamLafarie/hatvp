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
        #'PORT': '',
    }
}

# choose the database to use
db = DATABASES['default']

# construct an engine connection string
engine_string = "postgresql+psycopg2://{user}:{password}@{host}/{database}".format(
    user = db['USER'],
    password = db['PASSWORD'],
    host = db['HOST'],
    #port = db['PORT'],
    database = db['NAME'],
)

# create sqlalchemy engine
engine = create_engine(engine_string)

# read a table from database into pandas dataframe
df_col_names = ['ID Représentants', 'Adresse', 'Code Postal', 'Dernière publication active', 'Date première publication', 'Déclaration d\'appartenance à une organisation', 'Déclarations tiers', 'Dénomination', 'Identifiant National', 'Activités publiées', 'Page Facebook', 'Page Linkedin', 'Page Twitter', 'Site Web', 'Nom usage HATVP', 'Pays', 'Sigle HATVP', 'Type d\'identifiant national', 'Ville', 'Label catégorie organisation']
df = pd.read_sql_table('hatvp_informations_generales', engine)

PAGE_SIZE = 10


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

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

    html.Div([
            dcc.Dropdown(
                id='cp',
                options=[{'label': i, 'value': i} for i in df],
                placeholder='Sélectionner un champ',
                value='Code postal'
            )
    ]),

    html.Div([
        dcc.Dropdown(
            id='id_national',
            options=[{'label': j, 'value': j} for j in df['identifiant_national']],
            value=df['identifiant_national'][0],
            placeholder='identifiant_national',
            clearable=False,
        ),
        html.Div(id='output_container')
    ]),

    html.Div([
        dash_table.DataTable(
            id='table-for-informations',
            columns=[
                {'name': 'denomination', 'id': 'denomination', 'deletable': True},
                {'name': 'label_categorie_organisation', 'id': 'label_categorie_organisation', 'deletable': True},
                {'name': 'adresse', 'id': 'adresse', 'deletable': True},
                {'name': 'code_postal', 'id': 'code_postal', 'deletable': True},
                {'name': 'ville', 'id': 'ville', 'deletable': True},
                {'name': 'pays', 'id': 'pays', 'deletable': True},
            ],
            page_current=0,
            page_size=PAGE_SIZE,
            page_action='custom',

            sort_action='custom',
            sort_mode='single',
            sort_by=[]
        )
    ])
])

# Code pour le premier dropdown


# Code pour le deuxième dropdown
@app.callback(
    dash.dependencies.Output('output_container', 'children'),
    [dash.dependencies.Input('id_national', 'value')])
def update_output(value):
    index = find_index(df, value)
    adresse_organisme = df['adresse'][index]
    cp_organisme = df['code_postal'][index]
    ville_organisme = df['ville'][index]
    return 'The address of the selected national id is "{}"'.format(adresse_organisme) + ', the postal code is "{}"'.format(cp_organisme) + ' and the city is "{}"'.format(ville_organisme)


def find_index(dfobject, value):
    value_index = 0
    for row in dfobject['identifiant_national']:
        if row == value:
            return value_index
        value_index += 1


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
        dff_1 = df.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff_1 = df
    return dff_1.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')