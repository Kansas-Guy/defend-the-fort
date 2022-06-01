from django.urls import path

from . import views

urlpatterns = [
    # ex: /contact/
    path('', views.index, name='index'),
    # ex: /contact/Football
    path('student/<int:team_select>', views.student, name='student'),
    # ex: /contact/donor
    path('<str:student_name>/donor/', views.donors, name='donor')
]
