from django.contrib import admin
from .models import Action, Category, Priority

# Register your models here.
admin.site.register(Action)
admin.site.register(Category)
admin.site.register(Priority)
