from django.contrib import admin
from temporal.models import * 

# Register your models here.
class Modelo2Admin(admin.ModelAdmin):
    pass

admin.site.register(Modelo_2, Modelo2Admin)