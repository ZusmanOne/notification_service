from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClienList.as_view()),
    path('clients/<int:pk>/', views.ClientDetail.as_view()),
    path('distributions/', views.DistributionList.as_view()),
    path('distributions/<int:pk>/', views.DistributionDetail.as_view()),


]