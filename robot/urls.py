from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('create_robo', views.init_robo),
    re_path('move', views.navigate),
    re_path('home', views.blank_temp)
]
