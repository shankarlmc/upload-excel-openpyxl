from django.contrib import admin
from . models import ImportedData
# Register your models here.


@admin.register(ImportedData)
class DataAdmin(admin.ModelAdmin):
    list_display = ['name']
