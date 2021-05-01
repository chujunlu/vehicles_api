from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vehicles import views

urlpatterns = [
    path('cars', views.CarList.as_view(), name='car-list'),
    path('cars/<int:pk>', views.CarDetail.as_view(), name='car-detail'),
    path('trucks', views.TruckList.as_view(), name='truck-list'),
    path('trucks/<int:pk>', views.TruckDetail.as_view(), name='truck-detail'),
    path('boats', views.BoatList.as_view(), name='boat-list'),
    path('boats/<int:pk>', views.BoatDetail.as_view(), name='boat-detail'),
    path('users', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root)
]

urlpatterns = format_suffix_patterns(urlpatterns)
