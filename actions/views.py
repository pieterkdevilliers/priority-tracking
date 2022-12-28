from django.shortcuts import render, redirect
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


def add_action(request):
    if request.method == "POST":
        title = request.POST.get("action_title")
        priority = request.POST.get("priority_title")
        category = request.POST.get("category_title")
        Action.objects.create(title=title, priority=priority, category=category)

        return redirect('get_action_list')
    return render(request, 'actions/add_action.html')


def add_category(request):
    return render(request, 'actions/add_category.html')


def add_priority(request):
    return render(request, 'actions/add_priority.html')
