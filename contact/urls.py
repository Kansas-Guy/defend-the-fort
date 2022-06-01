from django.urls import path

from . import views

app_name = 'contact'
urlpatterns = [
    # ex: /contact/
    path('', views.index, name='index'),
    # ex: /contact/student
    # path('student/<str:team>/', views.student, name='student'),
    path('<str:team>', views.student, name='student'),
    # ex: /contact/donor
    path('donor/', views.donor, name='donor')
]
