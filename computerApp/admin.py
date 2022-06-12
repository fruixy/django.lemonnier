from django.contrib import admin

# Register your models here.

from .models import Infrastructure, Machine, Personnelle

admin.site.register(Machine)
admin.site.register(Infrastructure)
admin.site.register(Personnelle)
