from django.shortcuts import render, redirect
from .forms import ActionForm, CategoryForm, PriorityForm
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
    actionform = ActionForm()
    if request.method == "POST":
        actionform = ActionForm(request.POST)
        if actionform.is_valid():
            actionform.save()
            return redirect('/')


    context = {'actionform': actionform}
    return render(request, 'actions/add_action.html', context)

def add_category(request):
    categoryform = CategoryForm()
    if request.method == "POST":
        categoryform = CategoryForm(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('/categories/')


    context = {'categoryform': categoryform}
    return render(request, 'actions/add_category.html', context)


def add_priority(request):
    priorityform = PriorityForm()
    if request.method == "POST":
        priorityform = PriorityForm(request.POST)
        if priorityform.is_valid():
            priorityform.save()
            return redirect('/priorities/')


    context = {'priorityform': priorityform}
    return render(request, 'actions/add_priority.html', context)
