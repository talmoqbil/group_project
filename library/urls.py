from django.urls import path
from library import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('fiction/', views.Fiction, name='fiction'),
    path('about/', views.About, name='about'),
    path('bookpage/', views.BookPage, name='bookpage'),
    path('createreview/', views.CreateReview, name='createreview'),
    path('login/', views.user_login, name='login'),
    path('register/', views.Register, name='register'),
    path('reservations/', views.Reservations, name='reservations'),
    path('wishlist/', views.WishList, name='wishlist'),
    path('logout/', views.LogOut, name='logout'),

]
