from .models import Informations_generales
from .models import Dirigeants
from .models import Collaborateurs
from .models import Clients
from .models import Affiliations
from django.contrib import admin

admin.site.register(Informations_generales)
admin.site.register(Dirigeants)
admin.site.register(Collaborateurs)
admin.site.register(Clients)
admin.site.register(Affiliations)