"""
Views for the Actions App.
"""
from django.shortcuts import render, redirect
from .forms import ActionForm, CategoryForm, PriorityForm
from .models import Action, Category, Priority
# Create your views here.


def get_action_list(request):
    """
    Retrieves the action_list template.
    """
    actions = Action.objects.all()
    context = {
        "actions": actions
    }
    return render(request, 'actions/action_list.html', context)


def get_priorities_list(request):
    """
    Retrieves the priorities_list template.
    """
    priorities = Priority.objects.all()
    context = {
        "priorities": priorities
    }
    return render(request, 'actions/priorities_list.html', context)


def get_categories_list(request):
    """
    Retrieves the categories_list template.
    """
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'actions/categories_list.html', context)


def add_action(request):
    """
    Submits the ActionForm and Creates an Action
    """
    actionform = ActionForm()
    if request.method == "POST":
        actionform = ActionForm(request.POST)
        if actionform.is_valid():
            actionform.save()
            return redirect('/')

    context = {'actionform': actionform}
    return render(request, 'actions/add_action.html', context)


def update_action(request, pk):
    """
    Submits the ActionForm and Updates an Action
    """
    action = Action.objects.get(id=pk)
    actionform = ActionForm(instance=action)

    if request.method == "POST":
        actionform = ActionForm(request.POST, instance=action)
        if actionform.is_valid():
            actionform.save()
            return redirect('/')

    context = {'actionform': actionform}
    return render(request, 'actions/update_action.html', context)


def delete_action(request, pk):
    """
    Deletes the selected Action
    """
    action = Action.objects.get(id=pk)
    if request.method == "POST":
        action.delete()
        return redirect('/')

    context = {'item': action}
    return render(request, 'actions/delete_action.html', context)


def add_category(request):
    """
    Submits the CategoryForm and Creates a Category
    """
    categoryform = CategoryForm()
    if request.method == "POST":
        categoryform = CategoryForm(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('/categories/')

    context = {'categoryform': categoryform}
    return render(request, 'actions/add_category.html', context)


def update_category(request, pk):
    """
    Submits the CategoryForm and Updates a Category
    """
    category = Category.objects.get(id=pk)
    categoryform = CategoryForm(instance=category)

    if request.method == "POST":
        categoryform = CategoryForm(request.POST, instance=category)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('/categories/')

    context = {'categoryform': categoryform}
    return render(request, 'actions/update_category.html', context)


def delete_category(request, pk):
    """
    Deletes the selected Category
    """
    category = Category.objects.get(id=pk)
    if request.method == "POST":
        category.delete()
        return redirect('/categories/')

    context = {'item': category}
    return render(request, 'actions/delete_category.html', context)


def add_priority(request):
    """
    Submits the PriorityForm and Creates a Priority
    """
    priorityform = PriorityForm()
    if request.method == "POST":
        priorityform = PriorityForm(request.POST)
        if priorityform.is_valid():
            priorityform.save()
            return redirect('/priorities/')

    context = {'priorityform': priorityform}
    return render(request, 'actions/add_priority.html', context)


def update_priority(request, pk):
    """
    Submits the PriorityForm and Updates a Priority
    """
    priority = Priority.objects.get(id=pk)
    priorityform = PriorityForm(instance=priority)

    if request.method == "POST":
        priorityform = PriorityForm(request.POST, instance=priority)
        if priorityform.is_valid():
            priorityform.save()
            return redirect('/priorities/')

    context = {'priorityform': priorityform}
    return render(request, 'actions/update_priority.html', context)


def delete_priority(request, pk):
    """
    Deletes the selected Priority
    """
    priority = Priority.objects.get(id=pk)
    if request.method == "POST":
        priority.delete()
        return redirect('/priorities/')

    context = {'item': priority}
    return render(request, 'actions/delete_priority.html', context)
