from django.db import models
class Informations_generales(models.Model):
    representants_id = models.IntegerField(primary_key=True)
    adresse = models.CharField(null=True,blank=True,max_length=255)
    code_postal = models.CharField(null=True,blank=True,max_length=255)
    derniere_publication_activite = models.DateTimeField(null=True,blank=True) #A CHANGER EN DATE models.DateTimeField(null=True,blank=True,null=True,blank=True)
    date_premiere_publication = models.DateTimeField(null=True,blank=True) #A CHANGER EN DATE
    declaration_organisation_appartenance = models.BooleanField(null=True,blank=True)
    declaration_tiers = models.BooleanField(null=True,blank=True)
    denomination = models.CharField(null=True,blank=True,max_length=255)
    identifiant_national = models.CharField(null=True,blank=True,max_length=15)
    activites_publiees =  models.BooleanField(null=True,blank=True)
    page_facebook =models.CharField(null=True,blank=True,max_length=255)
    page_linkedin=models.CharField(null=True,blank=True,max_length=300)
    page_twitter=models.CharField(null=True,blank=True,max_length=255)
    site_web=models.CharField(null=True,blank=True,max_length=255)
    nom_usage_HATVP=models.CharField(null=True,blank=True,max_length=150)
    pays=models.CharField(null=True,blank=True,max_length=255)
    sigle_HATVP=models.CharField(null=True,blank=True,max_length=100)
    type_identifiant_national=models.CharField(null=True,blank=True,max_length=255)
    ville=models.CharField(null=True,blank=True,max_length=255)
    label_categorie_organisation=models.CharField(null=True,blank=True,max_length=255)

class Dirigeants(models.Model):
    civilite_dirigeant=models.CharField(null=True,blank=True,max_length=5)
    fonction_dirigeant=models.CharField(null=True,blank=True,max_length=255)
    nom_dirigeant=models.CharField(null=True,blank=True,max_length=255)
    prenom_dirigeant=models.CharField(null=True,blank=True,max_length=255)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    nom_prenom_dirigeant=models.CharField(null=True,blank=True,max_length=255)

class Collaborateurs(models.Model):
    civilite_collaborateur=models.CharField(null=True,blank=True,max_length=5)
    fonction_collaborateur=models.CharField(null=True,blank=True,max_length=255)
    nom_collaborateur=models.CharField(null=True,blank=True,max_length=255)
    prenom_collaborateur=models.CharField(null=True,blank=True,max_length=255)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    nom_prenom_collaborateur=models.CharField(null=True,blank=True,max_length=255)

class Clients(models.Model):
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    denomination_client=models.CharField(null=True,blank=True,max_length=255)
    identifiant_national_client=models.CharField(null=True,blank=True,max_length=255)
    type_identifiant_national_client=models.CharField(null=True,blank=True,max_length=255)

class Affiliations(models.Model):
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    denomination_affiliation=models.CharField(null=True,blank=True,max_length=5)
    identifiant_national_affiliation=models.CharField(null=True,blank=True,max_length=255)
    type_identifiant_national_affiliation=models.CharField(null=True,blank=True,max_length=255)

class Niveaux_intervention(models.Model):
    niveau_intervention=models.CharField(null=True,blank=True,max_length=20)
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
    montant_depense=models.CharField(null=True,blank=True,max_length=255)
    nombre_salaries=models.CharField(null=True,blank=True,max_length=255)
    chiffre_affaires = models.CharField(null=True,blank=True,max_length=255)
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
    identifiant_fiche = models.CharField(null=True,blank=True,max_length=255)
    objet_activite= models.CharField(null=True,blank=True,max_length=200)

class Domaines_intervention(models.Model):
    domaines_intervention_actions_menees=models.CharField(null=True,blank=True,max_length=255)
    activite_id = models.ForeignKey(Objets_activites,on_delete=models.CASCADE)

class Observations(models.Model):
    action_representation_interet_id = models.IntegerField(primary_key=True)
    activite_id = models.ForeignKey(Objets_activites,on_delete=models.CASCADE)
    observation = models.CharField(null=True,blank=True,max_length=250)

class Decisions_concernees(models.Model):
    decision_concernee = models.CharField(blank=True,max_length=255,null=True)
    action_representation_interet_id = models.ForeignKey(Observations,on_delete=models.CASCADE)

class Beneficiaires(models.Model):
    beneficiaire_action_menee = models.CharField(blank=True,max_length=100,null=True)
    action_representation_interet_id = models.ForeignKey(Observations,on_delete=models.CASCADE)
    action_menee_en_propre = models.IntegerField(null=True,blank=True,)

class Actions_menees(models.Model):
    action_menee= models.CharField(blank=True,max_length=100,null=True)
    action_representation_interet_id = models.ForeignKey(Observations,on_delete=models.CASCADE)
    action_menee_autre= models.CharField(null=True,blank=True,max_length=100)
   # other1= models.CharField(blank=True,max_length=200)
    #other2= models.CharField(blank=True,max_length=200)
    #other3= models.CharField(blank=True,max_length=200)
    #other4= models.CharField(blank=True,max_length=200)

class Secteur_activites(models.Model):
    secteur_activite = models.CharField(null=True,blank=True,max_length=200)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)





