from django.contrib import admin
from .models import Team, Roster, StudentInfo, Donor

# Register your models here.

admin.site.register([Team, Roster, StudentInfo, Donor])
