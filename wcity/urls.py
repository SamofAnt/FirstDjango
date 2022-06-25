from django.urls import path

from . import views


app_name = 'wcity'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:flat_id>/', views.detail, name='detail'),
    path('<int:flat_id>/rent/', views.rent, name='rent'),
]