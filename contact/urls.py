from django.urls import path

from . import views

urlpatterns = [
    # ex: /contact/
    path('', views.contact, name='contact'),
    path('team', views.team, name='team'),
    # ex: /contact/Football
    path('<int:team_select>/student', views.student, name='student'),
    # ex: /contact/donor
    path('<int:student_id>/donor', views.donors, name='donor'),
    path('coach', views.coach, name='coach'),
    path('coach/<int:team>/dashboard', views.dashboard, name='dashboard'),
]
