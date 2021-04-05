from django.shortcuts import render
from django.http import HttpResponse
from library.models import Genre, Book, Bookpage


def index(request):

    genre_list = Genre.objects.all()
    context_dict = {}
    context_dict['genres'] = genre_list
    return render(request, 'library/index.html', context=context_dict) 

def show_genre(request, genre_name_slug):

    context_dict = {}
    
    try:
        genre = Genre.objects.get(slug=genre_name_slug)
        books = Book.objects.filter(genre=genre)

        context_dict['books'] = books
        context_dict['genre'] = genre

    except Genre.DoesNotExist:
        context_dict['genre'] = None
        context_dict['books'] = None

    return render(request, 'library/genre.html', context=context_dict)



def Bookp(request, genre_name_slug):
    context_dict = {}
    
    try:
        genre = Genre.objects.get(slug=genre_name_slug)
        books = Book.objects.filter(genre=genre)
        bookpage = Bookpage.objects.all
        
        context_dict['books'] = books
        context_dict['genre'] = genre
        context_dict['bookpage'] = bookpage

    except Genre.DoesNotExist:
        context_dict['genre'] = None
        context_dict['books'] = None
        context_dict['bookpage'] = None

    return render(request, 'library/Bookp.html',context=context_dict)







def About(request):

    return render(request, 'library/about.html')


def BookPage(request):

    return render(request, 'library/bookpage.html')


def CreateReview(request):

    return render(request, 'library/createreview.html')


def LogIn(request):

    return render(request, 'library/login.html')


def Register(request):

    return render(request, 'library/register.html')


def Reservations(request):

    return render(request, 'library/Reservations.html')


def WishList(request):

    return render(request, 'library/WishList.html')


