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
df1 = pd.read_sql_table('hatvp_informations_generales', engine)
df_1 = df1.rename(columns={'representants_id': 'ID Représentants', 'adresse': 'Adresse', 'code_postal': 'Code Postal', 'derniere_publication_activite': 'Dernière publication active', 'date_premiere_publication': 'Date première publication', 'declaration_organisation_appartenance': 'Déclaration d\'appartenance à une organisation', 'declaration_tiers': 'Déclarations tiers', 'denomination': 'Dénomination', 'identifiant_national': 'Identifiant National', 'activites_publiees': 'Activités publiées', 'page_facebook': 'Page Facebook', 'page_linkedin': 'Page Linkedin', 'page_twitter': 'Page Twitter', 'site_web': 'Site Web', 'nom_usage_HATVP': 'Nom usage HATVP', 'pays': 'Pays', 'sigle_HATVP': 'Sigle HATVP', 'type_identifiant_national': 'Type d\'identifiant national', 'ville': 'Ville', 'label_categorie_organisation': 'Label catégorie organisation'})

# Page size for the dash table
PAGE_SIZE = 10

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
                options=[{'label': i, 'value': i} for i in df_1],
                placeholder='Sélectionner un champ',
                value='Code postal'
            )
    ]),

    html.Div([
        dcc.Dropdown(
            id='id_national',
            options=[{'label': j, 'value': j} for j in df_1['Identifiant National']],
            value=df_1['Identifiant National'][0],
            placeholder='Identifiant National',
            clearable=False,
        ),
        html.Div(id='output_container')
    ]),

    html.Div([
        dash_table.DataTable(
            id='table-for-informations',
            columns=[
                {'name': 'Dénomination', 'id': 'Dénomination', 'deletable': True},
                {'name': 'Label catégorie organisation', 'id': 'Label catégorie organisation', 'deletable': True},
                {'name': 'Adresse', 'id': 'Adresse', 'deletable': True},
                {'name': 'Code Postal', 'id': 'Code Postal', 'deletable': True},
                {'name': 'Ville', 'id': 'Ville', 'deletable': True},
                {'name': 'Pays', 'id': 'Pays', 'deletable': True},
            ],
            page_current=0,
            page_size=PAGE_SIZE,
            page_action='custom',

            sort_action='custom',
            sort_mode='single',
            sort_by=[]
        )
    ]),

#    dcc.Graph(
#        figure={
#            'data': [
#                go.Bar(
#                    x=df['nom'],
#                    y=df['nombres']
#                ),
#                go.Bar(
#                    x=df['nom'],
#                    y=df['argent']
#                )
#            ]

#        }

#    )
])

# Code pour le premier dropdown


# Code pour le deuxième dropdown
@app.callback(
    dash.dependencies.Output('output_container', 'children'),
    [dash.dependencies.Input('id_national', 'value')])
def update_output(value):
    index = find_index(df_1, value)
    adresse_organisme = df_1['Adresse'][index]
    cp_organisme = df_1['Code Postal'][index]
    ville_organisme = df_1['Ville'][index]
    return 'The address of the selected national id is "{}"'.format(adresse_organisme) + ', the postal code is "{}"'.format(cp_organisme) + ' and the city is "{}"'.format(ville_organisme)


def find_index(dfobject, value):
    value_index = 0
    for row in dfobject['Identifiant National']:
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
        dff_1 = df_1.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff_1 = df_1
    return dff_1.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')