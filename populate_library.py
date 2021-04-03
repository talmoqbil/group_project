import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')


import django
django.setup()
from library.models import Genre,Book


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    
    fiction_books = [
        {'title': 'Book Fiction 1',
         'url':'http://docs.python.org/3/tutorial/'},
        {'title':'Book Fiction 2',
         'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Book Fiction 3',
         'url':'http://www.korokithakis.net/tutorials/python/'} ]
    
    nonfiction_books = [
         {'title':'Book NonFiction 1',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Book NonFiction 2',
         'url':'http://www.djangorocks.com/'},
        {'title':'Book NonFiction 3',
         'url':'http://www.tangowithdjango.com/'} ]
    
    children_books = [
        {'title':'The Girl and the Dinosaur',
         'url':'http://127.0.0.1:8000/library/bookpage/'},
        {'title':'One Hundred Steps',
         'url':'http://flask.pocoo.org'} ]
    
    cats = {'FICTION': {'books': fiction_books},
            'NONFICTION': {'books': nonfiction_books},
            "CHILDREN'S": {'books': children_books}}
    
    # If you want to add more categories or pages,
    # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category
     # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_genre(cat)
        for p in cat_data['books']:
            add_book(c, p['title'], p['url'])
            

    # Print out the categories we have added.
    for c in Genre.objects.all():
        for p in Book.objects.filter(genre=c):
            print(f'- {c}: {p}')

def add_book(cat,title,url,views=0):
    p = Book.objects.get_or_create(genre=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_genre(name):
    c = Genre.objects.get_or_create(name=name)[0]
    c.save()
    return c

#Startexecutionhere!
if __name__=='__main__':
    print('Starting Library population script...')
    populate()
