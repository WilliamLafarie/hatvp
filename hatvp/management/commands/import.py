from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll
from django.contrib import admin
from hatvp.models import *
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

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        def date_function(value,type):
            if value=="":
                return None
            if type == 1:
                return datetime.strptime(str(value),'%d/%m/%Y %H:%M:%S')
            if type == 2:
                return datetime.strptime(str(value),'%d/%m/%Y')
                pass

        """
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
        """

        def trieFichierModeles(listFichier):
            listFichierTrie=[]
            fileInOrder=[]
            i=0
            for nbFichier,lFichier in enumerate(listFichier):
                for nbElem in range(len(listFichier)):
                    fileToTest=listFichier[nbElem].split("_",1)  
                    modelListInter = fileToTest[1].split('.')
                    if(nbFichier == int(fileToTest[0])):
                        fileInOrder.append(listFichier[nbElem])
                        listFichierTrie.append(modelListInter[0])
                
            return listFichierTrie,fileInOrder
            

        def destroyData(listModels):
            print("------- Debut destruction Data -------")
            for lenList in range(len(listModels)):
                listModels[lenList].objects.all().delete()
            print("------- Fin destruction Data -------")

        '''
        class Foobar:
            pass
        '''
        def str_to_class(list):
            modelsObject=[]
            for lenList in  range(len(list)):
                modelsObject.append(getattr(sys.modules[__name__], list[lenList]))
                #print(modelsObject)
            return modelsObject

        def recupChampList(listModels):
            listChamps=[[]]
            listIlistInfo=[]
            dico = {}
            for nbModels in range(len(listModels)):
                listInfo=listModels[nbModels]._meta.get_fields()
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
                nbFichier = nbFichier
                fichier = listeFichier[nbFichier]
            #objetNew = classModels[nbFichier]()
                allChamps = dicoModels[classModels[nbFichier]]
                #print("L'INDICE EST : {}".format(nbFichier))
                #print('OBJET UTILISE : {}'.format(objetNew))
                #print("CHAMPS SONT  : {}".format(allChamps))
                with open('fichierCsv/'+fichier,encoding="utf8") as csvfile:
                    print("--------------- DEBUT remplissage FICHIER {}  DANS reader test ---------------".format(fichier))
                    #read_file = reader(fichier)
                    #apps_data = list(read_file)
                    #rowcount = len(apps_data) #which incudes header row
                    #print("Total rows incuding header: " + str(rowcount))
                    spamreader = csv.reader(csvfile, delimiter=';')
                    next(spamreader,None)
                    i=0
                    for row in spamreader:
                        objetNew = classModels[nbFichier]()
                        #print("Object SELECTIONNE : {} ".format(objetNew))
                        #i = i+1
                        #print("LECTURE LIGNE : {}".format(i))
                        for tab in range(len(allChamps)):
                            i = i+1
                            type_variable=objetNew._meta.get_field(allChamps[tab]) #Nom du champs
                            if isinstance(type_variable,models.DateTimeField):
                                #print("AFFICHAGE LIGNEsssssssss : {}".format(row[tab]))
                                if(row[tab] ==""):
                                    row[tab]=None
                                else :
                                    try:
                                        row[tab] = datetime.strptime(row[tab], "%d/%m/%Y %H:%M:%S")
                                    except ValueError: # strptime raises a ValueError
                                        row[tab] = datetime.strptime(row[tab], "%Y-%m-%d")
                            #row[tab] = date_function(row[tab],1)
                            #print(len(allChamps))
                           # print("AFFICHAGE LIGNE : {}".format(row[tab]))
                            #print('voici TOUT LES CHAMPS DE : {} --------- : {}'.format(classModels[nbFichier],allChamps))
                            #if(objetNew not in listRefus):
                            # print('PARCOURIR LES CHAMPS UTILISES : {}'.format(allChamps[tab]))   
                            # print('OBJECT UTILISE  {}'.format(objetNew))
                            '''
                            if(allChamps[tab] == 'representants_id_id'):
                                #print("eeeeeeeerrrrrrrrrruuuuuuuuuuuuurrrrrrrrrrr")
                                #print(Informations_generales.objects.get(**{"representants_id": row[tab]}))
                                row[tab] = Informations_generales.objects.get(**{"representants_id": row[tab]})
                            if(allChamps[tab] == 'exercices_id_id'):
                                row[tab] = Exercices.objects.get(exercices_id = row[tab])
                            if(allChamps[tab] == 'activite_id_id'):
                                row[tab] = Objets_activites.objects.get(activite_id = row[tab])
                            if(allChamps[tab] == 'action_representation_interet_id_id'):
                                row[tab] = Observations.objects.get(action_representation_interet_id = row[tab])
                            '''
                            #print('OBJECT UTILISE  {}'.format(objetNew))   
                            setattr(objetNew, allChamps[tab],row[tab])     
                        objetNew.save()
                    # print(objetNew)
                csvfile.close()
                        #print('Nombre de ligner : {}'.format(len(row)))
                print("--------------- Fin remplissage  FICHIER {}  DANS reader test ---------------".format(fichier))

        #listvide  = recupChamp()
        #print(listvide)
        fichier=[]
        nouvelleListe=[]
        listFichier = os.listdir('./fichierCsv')
        #print(listFichier)
        dicoModels={}
        #listModel,fichierTrie = trieFichierModel(listFichier) #Recuperation des noms des models par ordre
        listModel,fichierTrie = trieFichierModeles(listFichier)
        print("listModel : {}".format(listModel))
        print("fichierTrie :  {}".format(fichierTrie))
        classModels = str_to_class(listModel) # Transformations des strings models en classe
        #print(listTrie)
        destroyData(classModels) #Destruction des datas de toutes les bases de donnes
        dicoModels = recupChampList(classModels)
        #print(dicoModels.keys())
        #print(listInfoModels)
        reader_test(fichierTrie,dicoModels)
        