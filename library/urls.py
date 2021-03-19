from django.urls import path
from library import views


app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
]
