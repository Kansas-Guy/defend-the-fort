from django.urls import path

from . import views

urlpatterns = [
    # ex: /contact/
    path('', views.index, name='index'),
    # ex: /contact/Football
    path('student/', views.student, name='student'),
    # ex: /contact/donor
    path('donor/', views.donor, name='donor')
]
