from django.urls import path
from . import views


urlpatterns = [
    path('addnotes', views.Add_Note),
    path('checknotes', views.Check_Note),
    path('main', views.Main_Page)
]