from django.db import models

# Create your models here.

class Informations_generales(models.Model):
    representants_id = models.IntegerField(primary_key=True)
    adresse = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=200)
    derniere_publication_activite = models.CharField(max_length=200) #A CHANGER EN DATE
    date_premiere_publication = models.CharField(max_length=200) #A CHANGER EN DATE
    declaration_organisation_appartenance = models.BooleanField(null=True,blank=True)
    declaration_tiers = models.BooleanField(null=True,blank=True)
    denomination = models.CharField(max_length=200)
    identifiant_national = models.CharField(max_length=200)
    activites_publiees =  models.BooleanField(null=True,blank=True)
    page_facebook =models.CharField(max_length=200)
    page_linkedin=models.CharField(max_length=200)
    page_twitter=models.CharField(max_length=200)
    site_web=models.CharField(max_length=200)
    nom_usage_HATVP=models.CharField(max_length=200)
    pays=models.CharField(max_length=200)
    sigle_HATVP=models.CharField(max_length=200)
    type_identifiant_national=models.CharField(max_length=200)
    ville=models.CharField(max_length=200)
    label_categorie_organisation=models.CharField(max_length=200)

class Dirigeants(models.Model):
    civilite_dirigeant=models.CharField(max_length=200)
    fonction_dirigeant=models.CharField(max_length=200)
    nom_dirigeant=models.CharField(max_length=200)
    prenom_dirigeant=models.CharField(max_length=200)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    nom_prenom_dirigeant=models.CharField(max_length=200)

class Collaborateurs(models.Model):
    civilite_collaborateur=models.CharField(max_length=200)
    fonction_collaborateur=models.CharField(max_length=200)
    nom_collaborateur=models.CharField(max_length=200)
    prenom_collaborateur=models.CharField(max_length=200)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    nom_prenom_collaborateur=models.CharField(max_length=200)

class Clients(models.Model):
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    denomination_client=models.CharField(max_length=200)
    identifiant_national_client=models.CharField(max_length=200)
    type_identifiant_national_client=models.CharField(max_length=200)

class Affiliations(models.Model):
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    denomination_affiliation=models.CharField(max_length=200)
    identifiant_national_affiliation=models.CharField(max_length=200)
    type_identifiant_national_affiliation=models.CharField(max_length=200)

class Niveaux_intervention(models.Model):
    niveau_intervention=models.CharField(max_length=200)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)

class Exercices(models.Model):
    exercices_id = models.IntegerField(primary_key=True)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    date_debut = models.CharField(max_length=200) #A CHANGER EN DATE
    date_fin = models.CharField(max_length=200) #A CHANGER EN DATE
    exercice_sans_activite=models.BooleanField()
    nombre_activites= models.IntegerField()
    declaration_incomplete=models.BooleanField()
    date_publication = models.CharField(max_length=200) #A CHANGER EN DATE
    exercice_sans_CA=models.BooleanField()
    montant_depense=models.CharField(max_length=200)
    nombre_salaries=models.FloatField()
    chiffre_affaires = models.CharField(max_length=200)
    annee_debut= models.IntegerField()
    annee_fin= models.IntegerField()
    montant_depense_inf= models.IntegerField()
    montant_depense_sup= models.IntegerField()
    ca_inf= models.IntegerField()
    ca_sup=models.FloatField()

class Objets_activites(models.Model):
    activite_id = models.IntegerField(primary_key=True)
    exercices_id = models.ForeignKey(Exercices,on_delete=models.CASCADE)
    date_publication_activite = models.CharField(max_length=200) #A CHANGER EN DATE
    identifiant_fiche = models.CharField(max_length=200)
    objet_activite= models.CharField(max_length=200)

class Domaines_intervention(models.Model):
    domaines_intervention_actions_menees=models.CharField(max_length=200)
    activite_id = models.ForeignKey(Objets_activites,on_delete=models.CASCADE)

class Observations(models.Model):
    action_representation_interet_id = models.IntegerField(primary_key=True)
    activite_id = models.ForeignKey(Objets_activites,on_delete=models.CASCADE)
    observation = models.CharField(max_length=200)

class Decisions_concernees(models.Model):
    decision_concernee = models.CharField(max_length=200)
    action_representation_interet_id = models.ForeignKey(Observations,on_delete=models.CASCADE)

class Beneficiaires(models.Model):
    beneficiaire_action_menee = models.CharField(max_length=200)
    action_representation_interet_id = models.ForeignKey(Observations,on_delete=models.CASCADE)
    action_menee_en_propre = models.IntegerField()

class Actions_menees(models.Model):
    action_menee= models.CharField(max_length=200)
    action_representation_interet_id = models.ForeignKey(Observations,on_delete=models.CASCADE)
    action_menee_autre= models.CharField(max_length=200)
    other1= models.CharField(max_length=200)
    other2= models.CharField(max_length=200)
    other3= models.CharField(max_length=200)
    other4= models.CharField(max_length=200)