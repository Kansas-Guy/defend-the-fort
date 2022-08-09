from django.urls import path

from . import views

urlpatterns = [
    # ex: /contact/
    path('', views.contact, name='contact'),
    path('team', views.team, name='team'),
    # ex: /contact/Football
    path('<int:team_select>/student', views.student, name='student'),
    path('<int:team_select>/<int:student_id>/student-info', views.student_info, name='student-info'),
    path('<int:student_id>/donor', views.donors, name='donor'),
    path('coach', views.coach, name='coach'),
    path('coach/<int:team>/dashboard', views.dashboard, name='dashboard'),
    path('<int:student_id>/donor/review', views.review, name='review'),
]
