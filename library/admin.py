from django.contrib import admin
from library.models import Genre, Book

# Add in this class to customise the Admin Interface
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface
admin.site.register(Genre, GenreAdmin)



# admin.site.register(Genre)
admin.site.register(Book)
