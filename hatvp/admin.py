from .models import *
#from .models import Dirigeants
#from .models import Collaborateurs
#from .models import Clients
#from .models import Affiliations
from django.contrib import admin

admin.site.register(Informations_generales)
admin.site.register(Dirigeants)
admin.site.register(Collaborateurs)
admin.site.register(Clients)
admin.site.register(Affiliations)
admin.site.register(Niveaux_intervention)
admin.site.register(Exercices)
admin.site.register(Objets_activites)
admin.site.register(Domaines_intervention)
admin.site.register(Observations)
admin.site.register(Decisions_concernees)
admin.site.register(Beneficiaires)
admin.site.register(Actions_menees)
admin.site.register(Secteur_activites)
