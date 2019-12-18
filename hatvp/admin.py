from django.contrib import admin
from .models import *
from django.contrib import admin
from django.db.models.fields.related import *
from django.db.models import *
import csv
import glob
import os
import re
from os.path import basename, splitext
import sys
from datetime import datetime



'''
Informations_generales,Dirigeants,Collaborateurs
Clients
Affiliations
Niveaux_intervention
Exercices
Objets_activites
Domaines_intervention
Observations
Decisions_concernees
Beneficiaires
Actions_menees



def date_function(value,type):
    if value=="":
        return None
    if type == 1:
        return datetime.strptime(str(value),'%d/%m/%Y %H:%M:%S')
    if type == 2:
        return datetime.strptime(str(value),'%d/%m/%Y')
        pass


def trieFichierModel(listFichier):
    i=0
    compteur1=1
    compteur2=0
    modelListInter=[]
    listFichierTrie=[]
    fileInOrder=[]
    while(i==0):
        fileToTest = listFichier[compteur2].split("_",1)
        if(int(fileToTest[0]) == compteur1):
            modelListInter = fileToTest[1].split('.')
            fileInOrder.append(listFichier[compteur2])
            listFichierTrie.append(modelListInter[0])
            compteur1+=1
            compteur2 = 0
        elif(compteur1 == len(listFichier)):
            return listFichierTrie,fileInOrder
            i=1
        else:
            compteur2+=1

def destroyData(listModels):
    for lenList in range(len(listModels)):
        listModels[lenList].objects.all().delete()


class Foobar:
    pass

def str_to_class(list):
    modelsObject=[]
    for lenList in  range(len(list)):
        modelsObject.append(getattr(sys.modules[__name__], list[lenList]))
        #print(modelsObject)
    return modelsObject

def recupChamp():
    listInfo=Collaborateurs._meta.get_fields()
    for i in range(len(listInfo)):
        if isinstance(listInfo[i],ManyToOneRel):
             #if hasattr(listInfo[7],'attname'):
            pass
        else:
            #print(i)
            listChamps.append(listInfo[i].attname)
    return listChamps

def recupChampList(listModels):
    listChamps=[[]]
    listIlistInfo=[]
    dico = {}
    for nbModels in range(len(listModels)):
        listInfo=listModels[nbModels]._meta.get_fields()
        #print(listIlistInfo)
        listIlistInfo=[]
        for nbInfo in range(len(listInfo)):
            if(hasattr(listInfo[nbInfo],'attname')):
                if(listInfo[nbInfo].attname !='id'):
                    listIlistInfo.append(listInfo[nbInfo].attname)
            else:
                pass
        dico[listModels[nbModels]] = listIlistInfo
    return dico

def reader_test(listeFichier,dicoModels):
    listRefus = [Informations_generales(),Exercices(),Objets_activites(),Observations()]
    #for nbFichier in range(len(listeFichier)):
    for nbFichier,fichier in enumerate(listeFichier):
        #print(listeFichier)
        fichier = listeFichier[nbFichier]
       #objetNew = classModels[nbFichier]()
        allChamps = dicoModels[classModels[nbFichier]]
        print("L'INDICE EST : {}".format(nbFichier))
        #print('OBJET UTILISE : {}'.format(objetNew))
        print("CHAMPS SONT  : {}".format(allChamps))
        with open('fichierCsv/'+fichier,encoding="utf8") as csvfile:
           
            print("--------------- DEBUT remplissage FICHIER {}  DANS reader test ---------------".format(fichier))
            #read_file = reader(fichier)
            #apps_data = list(read_file)
            #rowcount = len(apps_data) #which incudes header row
            #print("Total rows incuding header: " + str(rowcount))
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            #i=0
            for row in spamreader:
                objetNew = classModels[nbFichier]()
                print("Object SELECTIONNE : {} ".format(objetNew))
                #i = i+1
                #print("LECTURE LIGNE : {}".format(i))
                for tab in range(len(allChamps)):
                    
                    type_variable=objetNew._meta.get_field(allChamps[tab]) #Nom du champs
                    if isinstance(type_variable,models.DateTimeField):
                        if(row[tab] ==""):
                            row[tab]=None
                        else :
                            try:
                                row[tab] = datetime.strptime(row[tab], "%d/%m/%Y %H:%M:%S")
                            except ValueError: # strptime raises a ValueError
                                row[tab] = datetime.strptime(row[tab], "%Y-%m-%d")
                    
                    #row[tab] = date_function(row[tab],1)
                    #print(len(allChamps))
                    print("AFFICHAGE LIGNE : {}".format(row[tab]))
                    #print('voici TOUT LES CHAMPS DE : {} --------- : {}'.format(classModels[nbFichier],allChamps))
                    #if(objetNew not in listRefus):
                       # print('PARCOURIR LES CHAMPS UTILISES : {}'.format(allChamps[tab]))   
                       # print('OBJECT UTILISE  {}'.format(objetNew))
                    if(allChamps[tab] == 'representants_id_id'):
                        print("---------------DEDDAANNS  VALUE : {}".format(Info_generales.objects.get(representants_id = row[tab])))
                        row[tab] = Informations_generales.objects.get(representants_id = row[tab])
                    if(tab == 'exercices_id'):
                        row[tab] = Exercices.objects.get(exercices_id = row[tab])
                    if(tab == 'activite_id'):
                        row[tab] = Objets_activites.objects.get(activite_id = row[tab])
                    if(tab == 'action_representation_interet_id'):
                        row[tab] = Observations.objects.get(action_representation_interet_id = row[tab])
                    
                    print('OBJECT UTILISE  {}'.format(objetNew))   
                    setattr(objetNew, allChamps[tab],row[tab])
                    
                objetNew.save()
               # print(objetNew)
        csvfile.close()
                #print('Nombre de ligner : {}'.format(len(row)))
        #print("--------------- Fin remplissage  FICHIER {}  DANS reader test ---------------".format(fichier))

#listvide  = recupChamp()
#print(listvide)
fichier=[]
listFichier = os.listdir('./fichierCSV')
#print(listFichier)
dicoModels={}
listModel,fichierTrie = trieFichierModel(listFichier) #Recuperation des noms des models par ordre
classModels = str_to_class(listModel) # Transformations des strings models en classe
#print(listTrie)
destroyData(classModels) #Destruction des datas de toutes les bases de donnes
dicoModels = recupChampList(classModels)
#print(dicoModels.keys())
#print(listInfoModels)
reader_test(fichierTrie,dicoModels)


info_gen=['representants_id', 'adresse', 'code_postal', 'derniere_publication_activite', 'date_premiere_publication', 'declaration_organisation_appartenance', 'declaration_tiers', 'denomination', 'identifiant_national','activites_publiees','page_facebook', 'page_linkedin', 'page_twitter', 'site_web','nom_usage_HATVP', 'pays', 'sigle_HATVP', 'type_identifiant_national', 'ville', 'label_categorie_organisation']

class reader_test():
    
    #listFichier = os.listdir('./fichierCSV')
    #for nbFichier in range(0,2):
        #objetNew = classModels[nbFichier]()
    with open('fichierCsv/1_Informations_generales.csv',encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader,None)
        i=0
        for row in spamreader:
            objetInformations = Informations_generales()
            i = i+1
            print(i)
            for tab in range(len(info_gen)):
                setattr(objetInformations, info_gen[tab],row[tab])
            objetInformations.save()
    print("--------------- Fin remplissage reader test ---------------")   
#listvide = []

def modelsName():
    modeslListFinal=[]
    modeslListIntermediaire=[]
    listFichier = os.listdir('./fichierCSV')
    listOrder=[]
    for nbFichier in range(len(listFichier)):
        modeslListIntermediaire = listFichierTrie[nbFichier].split("_",1)
        modeslListIntermediaire = modeslListIntermediaire[1].split('.')
        modeslListFinal.append(modeslListIntermediaire[0])
    #print(modeslListFinal)
#print(Info_generales._meta.get_fields())

resultat= 0
resultat = dicoModels[Informations_generales]
for i in range(len(resultat)):
    print("Compteur : {} , et sa valeur : {}".format(i,resultat[i]))
#print(dicoModels[Informations_generales])

#def recuperation
#print(models[1].enums_all())


    #if hasattr(listInfo[7],'attname'):
#Informations_generales.objects.all().delete()
#Dirigeants.objects.all().delete()
info_gen=['representants_id', 'adresse', 'code_postal', 'derniere_publication_activite', 'date_premiere_publication', 'declaration_organisation_appartenance', 'declaration_tiers', 'denomination', 'identifiant_national','activites_publiees','page_facebook', 'page_linkedin', 'page_twitter', 'site_web','nom_usage_HATVP', 'pays', 'sigle_HATVP', 'type_identifiant_national', 'ville', 'label_categorie_organisation']

reader


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








#filepath = glob.glob('./fichierCSV/*.txt')
#DefaultStorage.listdir(filepath)
#print(FileSystemStorage('./fichierCSV/*.txt'))
listFichier = os.listdir('./fichierCSV')
print(Info_generales._meta.get_fields())
#filename = splitext(basename(filepath))[0]

# Register your models here.
#print(Info_generales.objects.all())
info_gen=['representants_id', 'adresse', 'code_postal', 'derniere_publication_activite', 'date_premiere_publication', 'declaration_organisation_appartenance', 'declaration_tiers', 'denomination', 'identifiant_national','activites_publiees','page_facebook', 'page_linkedin', 'page_twitter', 'site_web','nom_usage_HATVP', 'pays', 'sigle_HATVP', 'type_identifiant_national', 'ville', 'label_categorie_organisation']
dirig=['civilite_dirigeant', 'fonction_dirigeant', 'nom_dirigeant', 'prenom_dirigeant', 'representants_id', 'nom_prenom_dirigeant']

#listFile = ['fichierCsv/1_informations_generales.csv']
class recupChamp():
    with open('fichierCsv/1_informations_generales.csv',encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
#        for row in spamreader:
#            for t in row:


class reader_test():
    #print("longueur list : {}".format(len(info_gen)))
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
                #print(obj)
    print("--------------- Fin remplissage reader test ---------------")

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

class reader_dirigeants():
    for listFi in listFichier
        with open(listFi,encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            print
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
                  


 VERSIONS NOM OPE RECUPERATIONS MODELS
def modelsName():
    modeslListFinal=[]
    modeslListIntermediaire=[]
    listFichier = os.listdir('./fichierCSV')
    listOrder=[]
    for nbFichier in range(len(listFichier)):
        modeslListIntermediaire = listFichierTrie[nbFichier].split("_",1)
        modeslListIntermediaire = modeslListIntermediaire[1].split('.')
        modeslListFinal.append(modeslListIntermediaire[0])
    #print(modeslListFinal)
#print(Info_generales._meta.get_fields())



def reader_test():
    objetInformations = Informations_generales()
    listFichier = os.listdir('./fichierCSV')
    for nbFichier in range(0,2):
        objetNew = classModels[nbFichier]()
        with open('fichierCsv/'+listFichier[nbFichier],encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                for tab in range(len(info_gen)):
                    setattr(objetNewbj, info_gen[tab],row[tab])
                    objetNew.save()
        print("--------------- Fin remplissage reader test ---------------")

        '''