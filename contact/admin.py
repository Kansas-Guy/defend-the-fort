from django.contrib import admin
from .models import Team, Student, Donor

# Register your models here.

admin.site.register([Team, Student, Donor])
