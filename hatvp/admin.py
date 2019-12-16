from django.contrib import admin
from .models import Info_generales
from django.contrib import admin
import csv

# Register your models here.
info_gen=['representants_id', 'adresse', 'code_postal', 'derniere_publication_activite', 'date_premiere_publication', 'declaration_organisation_appartenance', 'declaration_tiers', 'denomination', 'identifiant_national','activites_publiees','page_facebook', 'page_linkedin', 'page_twitter', 'site_web','nom_usage_HATVP', 'pays', 'sigle_HATVP', 'type_identifiant_national', 'ville', 'label_categorie_organisation']
i=0
class reader_test():
    print("longueur list : {}".format(len(info_gen)))
    with open('fichierCsv/1_informations_generales.csv',encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader,None)
        for row in spamreader:
            obj = Info_generales()
            for tab in range(len(info_gen)):
                setattr(obj, info_gen[tab],row[tab])
                #print("TABLEAU REMPLIS :  {}".format(info_gen[tab]))
                #print('LES INFOS QUI REMPLISSENT : {}'.format(row[tab]))
                obj.save()
    #print("Row longueur : {}".format(i))