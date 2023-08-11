from django.contrib import admin
from .models import Team, Roster, Donor

# Register your models here.

admin.site.register([Team, Roster, Donor])
