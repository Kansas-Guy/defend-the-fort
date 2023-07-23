from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import DonorViewSet, RosterViewSet

router = DefaultRouter()
router.register('donors', DonorViewSet, basename='donors')
router.register('roster', RosterViewSet, basename='roster')

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
    path('donor/<int:donor_id>/update', views.donor_edit, name='donor_edit'),
    path('donor_review/<int:student_id>', views.donor_review, name='donor_review'),
    path('api/donors/<int:student_id>/', views.donors_for_student),
    path('api/approve/<int:donor_id>/', views.approve, name='approve'),
]
