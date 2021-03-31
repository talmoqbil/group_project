from django.contrib import admin
from library.models import Genre, Book
from library.models import UserProfile
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(UserProfile)
