"""
Views for the Actions App.
"""
import datetime
from datetime import timezone, date
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.core.mail import send_mail
from django.conf import settings
from .forms import ActionForm, CategoryForm, PriorityForm, CreateUserForm, UpdateActionForm
from .models import Action, Category, Priority
# Create your views here.


@login_required(login_url='login')
def get_action_list(request):
    """
    Retrieves the action_list template.
    """
    query = date.today()
    completed_actions_count = completed_actions(query)
    open_actions_count = open_actions(query)
    total_actions_count = total_actions(query)

    if total_actions_count > 0:

        total_action_time = tracked_time(query)
        total_seconds = int(tracked_seconds(total_action_time))
        converted_tracked_time = tracked_today(total_seconds)
        on_priority_count = on_priority_actions(query)
        off_priority_count = off_priority_actions(query)
        on_priority_time = on_priority_tracked_time(query)
        off_priority_time = off_priority_tracked_time(query)
        on_priority_seconds = int(tracked_seconds(on_priority_time))
        off_priority_seconds = int(tracked_seconds(off_priority_time))
        converted_on_priority_time = tracked_today(on_priority_seconds)
        converted_off_priority_time = tracked_today(off_priority_seconds)
        on_priority_perc = on_priority_calc(total_seconds, on_priority_seconds)
        off_priority_perc = off_priority_calc(
            total_seconds, off_priority_seconds)

    else:
        total_action_time = 0
        total_seconds = 0
        converted_tracked_time = 0
        on_priority_count = 0
        off_priority_count = 0
        on_priority_time = 0
        off_priority_time = 0
        on_priority_seconds = 0
        off_priority_seconds = 0
        converted_on_priority_time = 0
        converted_off_priority_time = 0
        on_priority_perc = 0
        off_priority_perc = 0

    all_time_tracked = tracked_time_all(query)
    all_time_seconds = int(tracked_seconds(all_time_tracked))
    all_time_on_priority_tracked = on_priority_tracked_all_time(query)
    all_time_off_priority_tracked = off_priority_tracked_all_time(query)
    all_time_on_priority_seconds = int(
            tracked_seconds(all_time_on_priority_tracked))
    all_time_off_priority_seconds = int(
            tracked_seconds(all_time_off_priority_tracked))
    on_priority_perc_all_time = on_priority_calc(
            all_time_seconds, all_time_on_priority_seconds)
    off_priority_perc_all_time = off_priority_calc(
            all_time_seconds, all_time_off_priority_seconds)

    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    actions = Action.objects.all()
    filtered_actions = Action.objects.filter(action_date=query, user=current_user)
    priorities = Priority.objects.all()
    context = {
        "username": username,
        "user_id": user_id,
        "filtered_actions": filtered_actions,
        "priorities": priorities,
        "completed_actions_count": completed_actions_count,
        "open_actions_count": open_actions_count,
        "total_actions_count": total_actions_count,
        "converted_tracked_time": converted_tracked_time,
        "on_priority_perc": on_priority_perc,
        "off_priority_perc": off_priority_perc,
        "converted_on_priority_time": converted_on_priority_time,
        "converted_off_priority_time": converted_off_priority_time,
        "on_priority_perc_all_time": on_priority_perc_all_time,
        "off_priority_perc_all_time": off_priority_perc_all_time,
    }
    return render(request, 'actions/action_list.html', context)


# Internal Functions

def open_actions(query):
    """
    Calculating the number of Open Actions.
    """
    open_actions = Action.objects.filter(
        done_status=False, action_date=query).count()
    return open_actions


def completed_actions(query):
    """
    Calculating the number of Completed Actions.
    """
    completed_actions = Action.objects.filter(
        done_status=True, action_date=query).count()
    return completed_actions


def total_actions(query):
    """
    Calculating the number of Actions.
    """
    total_actions = Action.objects.filter(action_date=query).count()
    return total_actions


def tracked_time(query):
    """
    Calculating the tracked time for the query date.
    """
    tracked_time = Action.objects.filter(
        action_date=query).aggregate(Sum('tracked_time'))
    return tracked_time


def tracked_seconds(total_action_time):
    """
    Converting tracked_time object into Seconds.
    """
    time_dict = total_action_time
    time = time_dict.get("tracked_time__sum")
    if time == None:
        tracked_seconds = 0
    else:
        tracked_seconds = total_action_time['tracked_time__sum']\
            .total_seconds()
    return tracked_seconds


def tracked_today(total_seconds):
    """
    Converting tracked_seconds into HH:MM:SS.
    """
    seconds = total_seconds
    minutes = seconds // 60
    hours = minutes // 60
    tracked_today = "%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60)
    return tracked_today


def on_priority_actions(query):
    """
    Calculating the number of On Priority Actions.
    """
    on_priority_actions = Action.objects.filter(
        action_date=query).exclude(priority__isnull=True).count()
    return on_priority_actions


def off_priority_actions(query):
    """
    Calculating the number of Off Priority Actions.
    """
    off_priority_actions = Action.objects.filter(
        action_date=query).exclude(priority__isnull=False).count()
    return off_priority_actions


def on_priority_calc(total_seconds, on_priority_seconds):
    """
    Calculating the % of On Priority Actions.
    """
    if total_seconds == 0:
        on_priority_calc = 0
    else:    
        on_priority_calc = (on_priority_seconds * 100) / total_seconds
    return on_priority_calc


def off_priority_calc(total_seconds, off_priority_seconds):
    """
    Calculating the % of Off Priority Actions.
    """
    if total_seconds == 0:
        off_priority_calc = 0
    else:
        off_priority_calc = (off_priority_seconds * 100) / total_seconds
    return off_priority_calc


def on_priority_tracked_time(query):
    """
    Calculating the time tracked for On Priority Actions.
    """
    on_priority_tracked_time = Action.objects.filter(
        action_date=query).exclude(priority__isnull=True).aggregate(
        Sum('tracked_time'))
    return on_priority_tracked_time


def off_priority_tracked_time(query):
    """
    Calculating the time tracked for Off Priority Actions.
    """
    off_priority_tracked_time = Action.objects.filter(
        action_date=query).exclude(priority__isnull=False).aggregate(
        Sum('tracked_time'))
    return off_priority_tracked_time


def tracked_time_all(query):
    """
    Calculating the tracked time for all time.
    """
    tracked_time_all = Action.objects.all().aggregate(Sum('tracked_time'))
    return tracked_time_all


def on_priority_tracked_all_time(query):
    """
    Calculating the time tracked for On Priority All Time.
    """
    on_priority_tracked_all_time = Action.objects.all().exclude(
        priority__isnull=True).aggregate(Sum('tracked_time'))
    return on_priority_tracked_all_time


def off_priority_tracked_all_time(query):
    """
    Calculating the time tracked for Off Priority All Time.
    """
    off_priority_tracked_all_time = Action.objects.all().exclude(
        priority__isnull=False).aggregate(Sum('tracked_time'))
    return off_priority_tracked_all_time


@login_required(login_url='login')
def get_filtered_action_list(request):
    """
    Retrieves the filtered action_list template.
    """
    query_dict = request.GET
    query = query_dict.get("action_date")
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    actions = Action.objects.all()
    filtered_actions = Action.objects.filter(action_date=query, user=current_user)
    context = {
        "username": username,
        "user_id": user_id,
        "query": query,
        "filtered_actions": filtered_actions
    }
    return render(request, 'actions/filtered_action_list.html', context)


@login_required(login_url='login')
def get_priorities_list(request):
    """
    Retrieves the priorities_list template.
    """
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    priorities = Priority.objects.filter(user=current_user)
    context = {
        "username": username,
        "user_id": user_id,
        "priorities": priorities
    }
    return render(request, 'actions/priorities_list.html', context)


@login_required(login_url='login')
def get_categories_list(request):
    """
    Retrieves the categories_list template.
    """
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    categories = Category.objects.filter(user=current_user)
    context = {
        "username": username,
        "user_id": user_id,
        "categories": categories
    }
    return render(request, 'actions/categories_list.html', context)


@login_required(login_url='login')
def add_action(request):
    """
    Submits the ActionForm and Creates an Action
    """
    actionform = ActionForm()
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    if request.method == "POST":
        actionform = ActionForm(request.POST)
        if actionform.is_valid():
            instance = actionform.save(commit=False)
            instance.user = request.user
            Action.category = instance.priority.category
            instance.save()
            messages.success(request, "Action added successfully")
            return redirect('/actions/')

    context = {
        'actionform': actionform,
        "username": username,
        "user_id": user_id
        }
    return render(request, 'actions/add_action.html', context)


@login_required(login_url='login')
def complete_action(request, pk):
    """
    Submits the ActionForm and Updates an Action
    """
    action = Action.objects.get(id=pk)
    action.done_status = not action.done_status
    action.save()
    messages.success(request, "Action status updated")
    return redirect('/actions/')


@login_required(login_url='login')
def complete_filtered_action(request, pk):
    """
    Submits the ActionForm and Updates an Action
    """
    action = Action.objects.get(id=pk)
    action.done_status = not action.done_status
    action.save()
    messages.success(request, "Action status updated")
    return redirect('/filtered-actions/')


@login_required(login_url='login')
def relist_action(request, pk):
    """
    Submits the ActionForm and Relists an Action
    """
    action = Action.objects.get(id=pk)
    action.action_date = date.today()
    action.save()
    messages.success(request, "Action relisted for today")
    return redirect('/filtered-actions/')


@login_required(login_url='login')
def update_action(request, pk):
    """
    Submits the UpdateActionForm and Updates an Action
    """
    action = Action.objects.get(id=pk)
    actionform = UpdateActionForm(instance=action)
    current_user = request.user
    user_id = current_user.id
    username = current_user.username

    if request.method == "POST":
        actionform = UpdateActionForm(request.POST, instance=action)
        if actionform.is_valid():
            actionform.save()
            messages.success(request, "Action updated successfully")
            return redirect('/actions/')

    context = {
        'actionform': actionform,
        "username": username,
        "user_id": user_id
        }
    return render(request, 'actions/update_action.html', context)


@login_required(login_url='login')
def delete_action(request, pk):
    """
    Deletes the selected Action
    """
    action = Action.objects.get(id=pk)
    if request.method == "POST":
        action.delete()
        messages.success(request, "Action deleted")
        return redirect('/actions/')

    context = {'item': action}
    return render(request, 'actions/delete_action.html', context)


@login_required(login_url='login')
def add_category(request):
    """
    Submits the CategoryForm and Creates a Category
    """
    categoryform = CategoryForm()
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    if request.method == "POST":
        categoryform = CategoryForm(request.POST)
        if categoryform.is_valid():
            instance = categoryform.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Category added successfully")
            return redirect('/categories/')

    context = {
        'categoryform': categoryform,
        "username": username,
        "user_id": user_id,
        }
    return render(request, 'actions/add_category.html', context)


@login_required(login_url='login')
def update_category(request, pk):
    """
    Submits the CategoryForm and Updates a Category
    """
    category = Category.objects.get(id=pk)
    categoryform = CategoryForm(instance=category)
    current_user = request.user
    user_id = current_user.id
    username = current_user.username

    if request.method == "POST":
        categoryform = CategoryForm(request.POST, instance=category)
        if categoryform.is_valid():
            categoryform.save()
            messages.success(request, "Category updated successfully")
            return redirect('/categories/')

    context = {
        'categoryform': categoryform,
        "username": username,
        "user_id": user_id,
        }
    return render(request, 'actions/update_category.html', context)


@login_required(login_url='login')
def delete_category(request, pk):
    """
    Deletes the selected Category
    """
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    category = Category.objects.get(id=pk)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Category deleted")
        return redirect('/categories/')

    context = {
        'item': category,
        "username": username,
        "user_id": user_id,
        }
    return render(request, 'actions/delete_category.html', context)


@login_required(login_url='login')
def add_priority(request):
    """
    Submits the PriorityForm and Creates a Priority
    """
    priorityform = PriorityForm()
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    if request.method == "POST":
        priorityform = PriorityForm(request.POST)
        if priorityform.is_valid():
            instance = priorityform.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Priority added successfully")
            return redirect('/priorities/')

    context = {
        'priorityform': priorityform,
        "username": username,
        "user_id": user_id,
        }
    return render(request, 'actions/add_priority.html', context)


@login_required(login_url='login')
def update_priority(request, pk):
    """
    Submits the PriorityForm and Updates a Priority
    """
    priority = Priority.objects.get(id=pk)
    priorityform = PriorityForm(instance=priority)
    current_user = request.user
    user_id = current_user.id
    username = current_user.username

    if request.method == "POST":
        priorityform = PriorityForm(request.POST, instance=priority)
        if priorityform.is_valid():
            priorityform.save()
            messages.success(request, "Priority updated successfully")
            return redirect('/priorities/')

    context = {
        'priorityform': priorityform,
        "username": username,
        "user_id": user_id,
        }
    return render(request, 'actions/update_priority.html', context)


@login_required(login_url='login')
def priority_active_status(request, pk):
    """
    Submits the PriorityForm and Updates an Active Status
    """
    priority = Priority.objects.get(id=pk)
    priority.activeStatus = not priority.activeStatus
    priority.save()
    messages.success(request, "Priority active status updated")
    return redirect('/priorities/')


@login_required(login_url='login')
def delete_priority(request, pk):
    """
    Deletes the selected Priority
    """
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    priority = Priority.objects.get(id=pk)
    if request.method == "POST":
        priority.delete()
        messages.success(request, "Priority deleted")
        return redirect('/priorities/')

    context = {
        'item': priority,
        "username": username,
        "user_id": user_id,
        }
    return render(request, 'actions/delete_priority.html', context)


def register_page(request):
    """
    Allows new user registrations
    """
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():

            # send welcome email
            username = request.POST['username']
            email = request.POST['email']
            subject = 'Welcome to Priority Tracker'
            message = f'Hi {username} thanks for checking out Priority Tracker.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # save new user
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            return redirect('/login/')

    context = {'form': form}
    return render(request, 'actions/register.html', context)


def login_page(request):
    """
    Allows user login
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/actions/')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'actions/login.html', context)


def logout_user(request):
    """
    Logs out the user
    """
    logout(request)
    return redirect('/login/')


@login_required(login_url='login')
def start_timer(request, pk):
    """
    Submits the ActionForm and sets the start time for an Action
    """
    action = Action.objects.get(id=pk)
    action.tracked_start = datetime.datetime.now(timezone.utc)
    action.tracking_status = True
    action.save()
    messages.success(request, "Timer started")
    return redirect('/actions/')


@login_required(login_url='login')
def stop_timer(request, pk):
    """
    Submits the ActionForm and sets the start time for an Action
    """
    action = Action.objects.get(id=pk)
    action.tracking_status = False
    action.tracked_stop = datetime.datetime.now(timezone.utc)
    if action.active_tracked_time is None:
        action.active_tracked_time = action.tracked_stop - action.tracked_start
        action.tracked_time = action.active_tracked_time
    else:
        action.active_tracked_time = action.tracked_stop - action.tracked_start
        action.tracked_time = action.tracked_time + action.active_tracked_time
    action.save()
    messages.success(request, "Timer stopped")
    return redirect('/actions/')


@login_required(login_url='login')
def tracking_status(request, pk):
    """
    Submits the ActionForm and Updates an Action Tracking Status
    """
    action = Action.objects.get(id=pk)
    action.tracking_status = not action.tracking_status
    action.save()
    return redirect('/actions/')

