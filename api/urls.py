from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('get/',views.getData),
    path('login/',obtain_auth_token),
    path('users/',views.getUsers),
    path('register/',views.RegisterUserAPIView.as_view()),
    path('restaurants/get',views.GetRestaurants.as_view()),
    path('restaurants/create',views.createRestaurant),
    path('restaurants/my', views.GetMyRestaurants.as_view()),
    path('rezervacija/create',views.createRez),
    path('rezervacija/get',views.GetRez.as_view())
]
