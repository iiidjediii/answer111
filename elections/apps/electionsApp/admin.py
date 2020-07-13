from django.contrib import admin

from .models import Vote, Person

admin.site.register(Vote)
admin.site.register(Person)