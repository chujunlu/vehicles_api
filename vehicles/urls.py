from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vehicles import views

urlpatterns = [
    path('cars/', views.CarList.as_view()),
    path('cars/<int:pk>/', views.CarDetail.as_view()),
    path('trucks/', views.TruckList.as_view()),
    path('trucks/<int:pk>/', views.TruckDetail.as_view()),
    path('boats/', views.BoatList.as_view()),
    path('boats/<int:pk>/', views.BoatDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
