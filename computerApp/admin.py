from django.contrib import admin

# Register your models here.

from .models import Infrastructure, Machine, Personnelle

#permet à l'admin de crée à partir des models
admin.site.register(Machine)
admin.site.register(Infrastructure)
admin.site.register(Personnelle)
