from django.shortcuts import render
from django.http import HttpResponse
from library.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


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

@login_required
def LogOut(request):
    logout(request)
    return redirect(reverse('library:index'))

def Register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()

            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'library/Register.html',
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})
        

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('library:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'library/login.html')


def Reservations(request):

    return render(request, 'library/Reservations.html')


def WishList(request):

    return render(request, 'library/WishList.html')


