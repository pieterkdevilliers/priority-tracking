from django.shortcuts import render
from .models import Action, Category, Priority


# Create your views here.


def get_action_list(request):
    actions = Action.objects.all()
    context = {
        "actions": actions
    }
    return render(request, 'actions/action_list.html', context)


def get_priorities_list(request):
    priorities = Priority.objects.all()
    context = {
        "priorities": priorities
    }
    return render(request, 'actions/priorities_list.html', context)


def get_categories_list(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'actions/categories_list.html', context)
