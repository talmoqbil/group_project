from django.urls import path
from library import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    
    #path('fiction/', views.Fiction, name='fiction'),
    #path('childrens/', views.Children, name='children'),
    #path('nonfiction/', views.nonFiction, name='nonfiction'),
    
    path('about/', views.About, name='about'),
    path('bookpage/', views.BookPage, name='bookpage'),
    path('createreview/', views.CreateReview, name='createreview'),
    path('login/', views.LogIn, name='login'),
    path('register/', views.Register, name='register'),
    path('reservations/', views.Reservations, name='reservations'),
    path('wishlist/', views.WishList, name='wishlist'),
    path('<slug:genre_name_slug>/',views.show_genre, name='show_genre'),

]
