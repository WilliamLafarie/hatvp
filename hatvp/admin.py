from django.contrib import admin
from .models import *
from django.contrib import admin
import csv

# Register your models here.
info_gen=['representants_id', 'adresse', 'code_postal', 'derniere_publication_activite', 'date_premiere_publication', 'declaration_organisation_appartenance', 'declaration_tiers', 'denomination', 'identifiant_national','activites_publiees','page_facebook', 'page_linkedin', 'page_twitter', 'site_web','nom_usage_HATVP', 'pays', 'sigle_HATVP', 'type_identifiant_national', 'ville', 'label_categorie_organisation']
dirig=['civilite_dirigeant', 'fonction_dirigeant', 'nom_dirigeant', 'prenom_dirigeant', 'representants_id', 'nom_prenom_dirigeant']

#listFile = ['fichierCsv/1_informations_generales.csv']
class reader_test():
    #print("longueur list : {}".format(len(info_gen)))
    with open('fichierCsv/1_informations_generales.csv',encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader,None)
        for row in spamreader:
            obj = Info_generales()
            obj.objects.all.delete()
            for tab in range(len(info_gen)):
                setattr(obj, info_gen[tab],row[tab])
                #print("TABLEAU REMPLIS :  {}".format(info_gen[tab]))
                #print('LES INFOS QUI REMPLISSENT : {}'.format(row[tab]))
                obj.save()
                #print(obj)
    print("Fin remplissage reader test")

class reader_dirigeants():
    with open('fichierCsv/2_dirigeants.csv',encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader,None)
        for row in spamreader:
            obj2 = Dirigeants()
            for tab in range(len(dirig)):
                if(row[tab] == 'representants_id'):
                    print("Ici primaire Kay")
                    print("value row tab{}".format(row[tab]))
                    row[tab] = Info_generales.objects.get(representants_id = row[tab])
                setattr(obj2, dirig[tab],row[tab])
                #print("TABLEAU REMPLIS :  {}".format(info_gen[tab]))
                #print('LES INFOS QUI REMPLISSENT : {}'.format(row[tab]))
                obj2.save()
                #print(obj)
   #if(champs_exercice[i]" == 'representans-id'):
#    row[i] = Info_generales.objects.get(representans_id = row[i])
