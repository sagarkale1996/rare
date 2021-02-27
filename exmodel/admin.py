from django.contrib import admin
from .models import exuser

# Register your models here.
class exuseradmin(admin.ModelAdmin):
    list_display = ['user','age','mob_no','address']
admin.site.register(exuser,exuseradmin)

