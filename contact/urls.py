from django.urls import path

from . import views

urlpatterns = [
    # ex: /contact/
    path('', views.contact, name='contact'),
    path('team', views.team, name='team'),
    # ex: /contact/Football
    path('<int:team_select>/student', views.student, name='student'),
    # ex: /contact/donor
    path('<str:student_name>/donor', views.donors, name='donor')
]
