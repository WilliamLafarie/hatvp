import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
from django_plotly_dash import DjangoDash
import pandas as pd
from sqlalchemy import create_engine
import os
from functools import reduce

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

# read a table from database into pandas dataframe, and do it for all tables
df1 = pd.read_sql_table('hatvp_informations_generales', engine)
df_1 = df1.rename(columns={'representants_id': 'ID du représentant', 'adresse': 'Adresse', 'code_postal': 'Code Postal', 'derniere_publication_activite': 'Dernière publication active', 'date_premiere_publication': 'Date première publication', 'declaration_organisation_appartenance': 'Déclaration d\'appartenance à une organisation', 'declaration_tiers': 'Déclarations tiers', 'denomination': 'Dénomination', 'identifiant_national': 'Identifiant National', 'activites_publiees': 'Activités publiées', 'page_facebook': 'Page Facebook', 'page_linkedin': 'Page Linkedin', 'page_twitter': 'Page Twitter', 'site_web': 'Site Web', 'nom_usage_HATVP': 'Nom usage HATVP', 'pays': 'Pays', 'sigle_HATVP': 'Sigle HATVP', 'type_identifiant_national': 'Type d\'identifiant national', 'ville': 'Ville', 'label_categorie_organisation': 'Label catégorie organisation'})

df2 = pd.read_sql_table('hatvp_dirigeants', engine)
df_2 = df2.rename(columns={'id': 'ID', 'civilite_dirigeant': 'Civilité du dirigeant', 'fonction_dirigeant': 'Fonction du dirigeant', 'nom_dirigeant': 'Nom du dirigeant', 'nom_prenom_dirigeant': 'Nom et prénom du dirigeant', 'prenom_dirigeant': 'Prénom du dirigeant', 'representants_id_id': 'ID du représentant'})

df3 = pd.read_sql_table('hatvp_collaborateurs', engine)
df_3 = df3.rename(columns={'id': 'ID', 'civilite_collaborateur': 'Civilité du collaborateur', 'fonction_collaborateur': 'Fonction du collaborateur', 'nom_collaborateur': 'Nom du collaborateur', 'nom_prenom_collaborateur': 'Nom et prénom du collaborateur', 'prenom_collaborateur': 'Prénom du collaborateur', 'representants_id_id': 'ID du représentant'})


df4 = pd.read_sql_table('hatvp_clients', engine)
df_4 = df4.rename(columns={'id': 'ID', 'denomination_client': 'Dénomination du client', 'identifiant_national_client': 'Identifiant National du client', 'representants_id_id': 'ID du représentant', 'type_identifiant_national_client': 'Type d\'identifiant national du client'})

df5 = pd.read_sql_table('hatvp_affiliations', engine)
df_5 = df5.rename(columns={'id': 'ID', 'denomination_affiliation': 'Dénomination de l\'affiliation', 'identifiant_national_affiliation': 'Identifiant national de l\'affiliation', 'representants_id_id': 'ID du représentant', 'type_identifiant_national_affiliation': 'Type d\'identifiant national de l\'affiliation'})

df6 = pd.read_sql_table('hatvp_niveaux_intervention', engine)
df_6 = df6.rename(columns={'id': 'ID', 'niveau_intervention': 'Niveau de l\'intervention', 'representants_id_id': 'ID du représentant'})

df7 = pd.read_sql_table('hatvp_domaines_intervention', engine)
df_7 = df7.rename(columns={'id': 'ID', 'activite_id_id': 'ID de l\'activité', 'domaines_intervention_actions_menees': 'Domaine d\intervention de l\'action menée'})

df8 = pd.read_sql_table('hatvp_objets_activites', engine)
df_8 = df8.rename(columns={'activite_id': 'ID de l\'activité', 'date_publication_activite': 'Date de la publication de l\'activité', 'exercices_id_id': 'ID de l\'exercice', 'identifiant_fiche': 'ID de la fiche', 'objet_activite': 'Object de l\'activité'})

df9 = pd.read_sql_table('hatvp_secteur_activites', engine)
df_9 = df9.rename(columns={'id': 'ID', 'representants_id_id': 'ID du représentant', 'secteur_activite': 'Secteur d\'activité'})

df10 = pd.read_sql_table('hatvp_actions_menees', engine)
df_10 = df10.rename(columns={'id': 'ID', 'action_menee': 'Action menée', 'action_menee_autre': 'Autre action menée', 'action_representation_interet_id_id': 'ID de l\'action de représentation d\'intérêt'})

df11 = pd.read_sql_table('hatvp_beneficiaires', engine)
df_11 = df11.rename(columns={'id': 'ID', 'action_menee_en_propre': 'Action menée en propre', 'action_representation_interet_id_id': 'ID de l\'action de représentation d\'intérêt', 'beneficiaire_action_menee': 'Bénéficiaire de l\'action menée'})

df12 = pd.read_sql_table('hatvp_decisions_concernees', engine)
df_12 = df12.rename(columns={'id': 'ID', 'action_representation_interet_id_id': 'ID de l\'action de représentation d\'intérêt', 'decision_concernee': 'Décision concernée'})

df14 = pd.read_sql_table('hatvp_observations', engine)
df_14 = df14.rename(columns={'action_representation_interet_id': 'ID de l\'action de représentation d\'intérêt', 'activite_id_id': 'ID de l\'activité', 'observation': 'Observation'})

df15 = pd.read_sql_table('hatvp_exercices', engine)
df_15 = df15.rename(columns={'exercices_id': 'ID de l\'exercice', 'annee_debut': 'Année de début', 'annee_fin': 'Année de fin', 'ca_inf': 'Chiffre d\'affaire inférieur', 'ca_sup': 'Chiffre d\'affaire supérieur', 'chiffre_affaires': 'Chiffre d\'affaire', 'date_debut': 'Date de début', 'date_fin': 'Date de fin', 'date_publication': 'Date de publication', 'declaration_incomplete': 'Déclaration incomplète', 'exercice_sans_CA': 'Exercice sans chiffre d\'affaire', 'exercice_sans_activite': 'Exercice sans activité', 'montant_depense': 'Montant de la dépense', 'montant_depense_inf': 'Montant de dépense inférieur', 'montant_depense_sup': 'Montant de dépense supérieur', 'nombre_activite': 'Nombre d\'activité', 'nombre_salaries': 'Nombre de salariés', 'representants_id_id': 'ID du représentant'})

# Jointure entre les 15 tables en procédant par étape
# Jointure des tables sur representant_id
list_df_rep_id_1 = [df_1, df_2, df_3, df_4, df_5, df_6]
df_all_1 = reduce(lambda  left,right: pd.merge(left,right,on=['ID du représentant'],how='outer'), list_df_rep_id_1)


# Jointure des tables sur actio_representation_interet_id
list_df_ari_id = [df_10, df_11, df_12]
df_all_2 = reduce(lambda left, right: pd.merge(left, right, on=['ID de l\'action de représentation d\'intérêt'], how='outer'), list_df_ari_id)

# Jointure des tables sur activite_id
list_df_activite_id = [df_7, df_8, df_14]
df_activite_id = reduce(lambda left, right: pd.merge(left,right, on=['ID de l\'activité'], how='outer'), list_df_activite_id)
df_activite_id_15 = pd.merge(df_activite_id, df_15, on=['ID de l\'exercice'], how='outer')
df_all_3 = pd.merge(df_activite_id_15, df_9, on=['ID du représentant'], how='outer')


# Page size for the dash table
PAGE_SIZE = 10

app = DjangoDash('SimpleExample')

app.layout = html.Div([
   html.Div([
        dcc.Dropdown(
            id='dp-df1',
            options=[{'label': i, 'value': i} for i in df_1],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df2',
            options=[{'label': i, 'value': i} for i in df_2],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df3',
            options=[{'label': i, 'value': i} for i in df_3],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df4',
            options=[{'label': i, 'value': i} for i in df_4],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df5',
            options=[{'label': i, 'value': i} for i in df_5],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df6',
            options=[{'label': i, 'value': i} for i in df_6],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df7',
            options=[{'label': i, 'value': i} for i in df_7],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df8',
            options=[{'label': i, 'value': i} for i in df_8],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df9',
            options=[{'label': i, 'value': i} for i in df_9],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df10',
            options=[{'label': i, 'value': i} for i in df_10],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df11',
            options=[{'label': i, 'value': i} for i in df_11],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df12',
            options=[{'label': i, 'value': i} for i in df_12],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df14',
            options=[{'label': i, 'value': i} for i in df_14],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df15',
            options=[{'label': i, 'value': i} for i in df_15],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df_all_1',
            options=[{'label': i, 'value': i} for i in df_all_1],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df_all_2',
            options=[{'label': i, 'value': i} for i in df_all_2],
            placeholder='Sélectionner un champ',
        )
    ]),

    html.Div([
        dcc.Dropdown(
            id='dp_df_all_3',
            options=[{'label': i, 'value': i} for i in df_all_3],
            placeholder='Sélectionner un champ',
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