from ast import Div
from django.contrib import admin
from .models import contacto, producto

# Register your models here.S

class AdminProd(admin.ModelAdmin):
    list_display=["nombre","marca","precio"]
    list_editable=["precio"]
    search_fields=["nombre"]
    list_filter=["marca"]
    list_per_page=6



admin.site.register(contacto)
admin.site.register(producto,AdminProd)



