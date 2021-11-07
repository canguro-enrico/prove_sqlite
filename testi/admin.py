from django.contrib import admin

# Register your models here.
from .models import Autore, Testo
admin.site.register(Autore)
#admin.site.register(Editore)
admin.site.register(Testo)
