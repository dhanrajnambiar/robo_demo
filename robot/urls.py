from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('create_robo', views.init_robo),
    re_path('shift', views.navigate),
    re_path('sample_temp', views.blank_temp)
]
