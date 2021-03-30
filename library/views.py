from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    # context_dict = {'boldmessage': 'This is the bold message'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'library/index.html') #, context=context_dict


def About(request):

    return render(request, 'library/about.html')


def BookPage(request):

    return render(request, 'library/bookpage.html')

def CreateReview(request):

    return render(request, 'library/createreview.html')

def Fiction(request):

    return render(request, 'library/fiction.html')

def LogIn(request):

    return render(request, 'library/login.html')


def Register(request):

    return render(request, 'library/register.html')


def Reservations(request):

    return render(request, 'library/Reservations.html')


def WishList(request):

    return render(request, 'library/WishList.html')


