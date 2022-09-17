from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('distributions', views.DistributionViewSet, basename='distributions')
urlpatterns = router.urls

urlpatterns += [
    path('clients/', views.ClienList.as_view(), name='client-list'),
    path('clients/<int:pk>/', views.ClientDetail.as_view(), name='clien-detail'),
    path('statistic/', views.general_statistic, name='statistic'),


]

