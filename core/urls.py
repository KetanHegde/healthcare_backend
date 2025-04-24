from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path('auth/register/', views.RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),

    path('patients/', views.PatientListCreateView.as_view()),
    path('patients/<int:pk>/', views.PatientDetailView.as_view()),

    path('doctors/', views.DoctorListCreateView.as_view()),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view()),

    path('mappings/', views.MappingListCreateView.as_view()),                      
    path('mappings/<int:patient_id>/', views.MappingByPatientView.as_view()),      
    path('mappings/delete/<int:pk>/', views.MappingDeleteView.as_view()),          
]