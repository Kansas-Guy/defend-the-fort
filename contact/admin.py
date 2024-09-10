from django.contrib import admin
from .models import Project, Members, Contacts

# Register your models here.

admin.site.register([Project, Members, Contacts])
