from django.db import models

class Informations_generales(models.Model):
    representants_id = models.IntegerField(primary_key=True)
    adresse = models.CharField(null=True,blank=True,max_length=170)
    code_postal = models.CharField(null=True,blank=True,max_length=20)
    derniere_publication_activite = models.DateTimeField(null=True,blank=True) #A CHANGER EN DATE models.DateTimeField(null=True,blank=True,null=True,blank=True)
    date_premiere_publication = models.DateTimeField(null=True,blank=True) #A CHANGER EN DATE
    declaration_organisation_appartenance = models.BooleanField(null=True,blank=True)
    declaration_tiers = models.BooleanField(null=True,blank=True)
    denomination = models.CharField(null=True,blank=True,max_length=135)
    identifiant_national = models.CharField(null=True,blank=True,max_length=20)
    activites_publiees =  models.BooleanField(null=True,blank=True)
    page_facebook =models.CharField(null=True,blank=True,max_length=150)
    page_linkedin=models.CharField(null=True,blank=True,max_length=280)
    page_twitter=models.CharField(null=True,blank=True,max_length=105)
    site_web=models.CharField(null=True,blank=True,max_length=115)
    nom_usage_HATVP=models.CharField(null=True,blank=True,max_length=127)
    pays=models.CharField(null=True,blank=True,max_length=21)
    sigle_HATVP=models.CharField(null=True,blank=True,max_length=60)
    type_identifiant_national=models.CharField(null=True,blank=True,max_length=15)
    ville=models.CharField(null=True,blank=True,max_length=60)
    label_categorie_organisation=models.CharField(null=True,blank=True,max_length=80)

class Dirigeants(models.Model):
    civilite_dirigeant=models.CharField(null=True,blank=True,max_length=13)
    fonction_dirigeant=models.CharField(null=True,blank=True,max_length=119)
    nom_dirigeant=models.CharField(null=True,blank=True,max_length=39)
    prenom_dirigeant=models.CharField(null=True,blank=True,max_length=31)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    nom_prenom_dirigeant=models.CharField(null=True,blank=True,max_length=45)

class Collaborateurs(models.Model):
    civilite_collaborateur=models.CharField(null=True,blank=True,max_length=13)
    fonction_collaborateur=models.CharField(null=True,blank=True,max_length=200)
    nom_collaborateur=models.CharField(null=True,blank=True,max_length=42)
    prenom_collaborateur=models.CharField(null=True,blank=True,max_length=51)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    nom_prenom_collaborateur=models.CharField(null=True,blank=True,max_length=70)

class Clients(models.Model):
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    denomination_client=models.CharField(null=True,blank=True,max_length=135)
    identifiant_national_client=models.CharField(null=True,blank=True,max_length=20)
    type_identifiant_national_client=models.CharField(null=True,blank=True,max_length=15)

class Affiliations(models.Model):
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    denomination_affiliation=models.CharField(null=True,blank=True,max_length=145)
    identifiant_national_affiliation=models.CharField(null=True,blank=True,max_length=20)
    type_identifiant_national_affiliation=models.CharField(null=True,blank=True,max_length=15)

class Niveaux_intervention(models.Model):
    niveau_intervention=models.CharField(null=True,blank=True,max_length=18)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)

class Exercices(models.Model):
    exercices_id = models.IntegerField(primary_key=True)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    date_debut = models.DateTimeField(null=True,blank=True) # A DATER
    date_fin = models.DateTimeField(null=True,blank=True) # A DATER
    exercice_sans_activite=models.BooleanField(null=True,blank=True)
    nombre_activite = models.IntegerField(null=True,blank=True)
    declaration_incomplete=models.BooleanField(null=True,blank=True)
    date_publication = models.DateTimeField(null=True,blank=True) #A CHANGER EN DATE
    exercice_sans_CA=models.BooleanField(null=True,blank=True)
    montant_depense=models.CharField(null=True,blank=True,max_length=42)
    nombre_salaries=models.CharField(null=True,blank=True,max_length=17)
    chiffre_affaires = models.CharField(null=True,blank=True,max_length=100)
    annee_debut= models.IntegerField(null=True,blank=True)
    annee_fin= models.IntegerField(null=True,blank=True)
    montant_depense_inf= models.IntegerField(null=True,blank=True)
    montant_depense_sup= models.IntegerField(null=True,blank=True)
    ca_inf= models.IntegerField(null=True,blank=True)
    ca_sup=models.FloatField(null=True,blank=True)

class Objets_activites(models.Model):
    activite_id = models.IntegerField(primary_key=True)
    exercices_id = models.ForeignKey(Exercices,on_delete=models.CASCADE)
    date_publication_activite =models.DateTimeField(null=True,blank=True) #A CHANGER EN DATE
    identifiant_fiche = models.CharField(null=True,blank=True,max_length=18)
    objet_activite= models.CharField(null=True,blank=True,max_length=210)

class Domaines_intervention(models.Model):
    domaines_intervention_actions_menees=models.CharField(null=True,blank=True,max_length=55)
    activite_id = models.ForeignKey(Objets_activites,on_delete=models.CASCADE)

class Observations(models.Model):
    action_representation_interet_id = models.IntegerField(primary_key=True)
    activite_id = models.ForeignKey(Objets_activites,on_delete=models.CASCADE)
    observation = models.CharField(null=True,blank=True,max_length=710)

class Decisions_concernees(models.Model):
    decision_concernee = models.CharField(blank=True,max_length=100,null=True)
    action_representation_interet_id = models.ForeignKey(Observations,on_delete=models.CASCADE)

class Beneficiaires(models.Model):
    beneficiaire_action_menee = models.CharField(blank=True,max_length=135,null=True)
    action_representation_interet_id = models.ForeignKey(Observations,on_delete=models.CASCADE)
    action_menee_en_propre = models.IntegerField(null=True,blank=True,)

class Actions_menees(models.Model):
    action_menee= models.CharField(blank=True,max_length=123,null=True)
    action_representation_interet_id = models.ForeignKey(Observations,on_delete=models.CASCADE)
    action_menee_autre= models.CharField(null=True,blank=True,max_length=210)


class Secteur_activites(models.Model):
    secteur_activite = models.CharField(null=True,blank=True,max_length=59)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)





