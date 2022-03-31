from django.contrib import admin
from userapp.models import Userapp_user

class Userapp_userAdmin(admin.ModelAdmin):
    fields = ['username']
admin.site.register(Userapp_user,Userapp_userAdmin)
