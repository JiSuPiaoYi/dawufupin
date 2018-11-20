from django.contrib import admin

from .models import FourInOneDataForm,FourInOneAdditionalForm

# Register your models here.

admin.site.register(FourInOneDataForm)    #四位一体表
admin.site.register(FourInOneAdditionalForm)    #四位一体附加表