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
from .forms import ActionForm, CategoryForm, PriorityForm, CreateUserForm
from .models import Action, Category, Priority
# Create your views here.


@login_required(login_url='login')
def get_action_list(request):
    """
    Retrieves the action_list template.
    """
    query = date.today()
    completedActionsCount = completedActions(query)
    openActionsCount = openActions(query)
    totalActionsCount = totalActions(query)

    if totalActionsCount > 0:

        totalActionTime = trackedTime(query)
        totalSeconds = int(trackedSeconds(totalActionTime))
        convertedTrackedTime = trackedToday(totalSeconds)
        onPriorityCount = onPriorityActions(query)
        offPriorityCount = offPriorityActions(query)
        onPriorityTime = onPriorityTrackedTime(query)
        offPriorityTime = offPriorityTrackedTime(query)
        onPrioritySeconds = int(trackedSeconds(onPriorityTime))
        offPrioritySeconds = int(trackedSeconds(offPriorityTime))
        convertedOnPriorityTime = trackedToday(onPrioritySeconds)
        convertedOffPriorityTime = trackedToday(offPrioritySeconds)
        onPriorityPerc = onPriorityCalc(totalSeconds, onPrioritySeconds)
        offPriorityPerc = offPriorityCalc(totalSeconds, offPrioritySeconds)
        allTimeTracked = trackedTimeAll(query)
        allTimeSeconds = int(trackedSeconds(allTimeTracked))
        allTimeOnPriorityTracked = onPriorityTrackedAllTime(query)
        allTimeOffPriorityTracked = offPriorityTrackedAllTime(query)
        allTimeOnPrioritySeconds = int(trackedSeconds(allTimeOnPriorityTracked))
        allTimeOffPrioritySeconds = int(trackedSeconds(allTimeOffPriorityTracked))
        onPriorityPercAllTime = onPriorityCalc(allTimeSeconds, allTimeOnPrioritySeconds)
        offPriorityPercAllTime = offPriorityCalc(allTimeSeconds, allTimeOffPrioritySeconds)

    else:
        totalActionTime = 0
        totalSeconds = 0
        convertedTrackedTime = 0
        onPriorityCount = 0
        offPriorityCount = 0
        onPriorityTime = 0
        offPriorityTime = 0
        onPrioritySeconds = 0
        offPrioritySeconds = 0
        convertedOnPriorityTime = 0
        convertedOffPriorityTime = 0
        onPriorityPerc = 0
        offPriorityPerc = 0
        allTimeTracked = 0
        allTimeSeconds = 0
        allTimeOnPriorityTracked = 0
        allTimeOffPriorityTracked = 0
        allTimeOnPrioritySeconds = 0
        allTimeOffPrioritySeconds = 0
        onPriorityPercAllTime = 0
        offPriorityPercAllTime = 0

    actions = Action.objects.all()
    filteredActions = Action.objects.filter(actionDate=query)
    priorities = Priority.objects.all()
    context = {
        "actions": actions,
        "query": query,
        "filteredActions": filteredActions,
        "priorities": priorities,
        "completedActionsCount": completedActionsCount,
        "openActionsCount": openActionsCount,
        "totalActionTime": totalActionTime,
        "totalActionsCount": totalActionsCount,
        "convertedTrackedTime": convertedTrackedTime,
        "onPriorityCount": onPriorityCount,
        "offPriorityCount": offPriorityCount,
        "onPriorityPerc": onPriorityPerc,
        "offPriorityPerc": offPriorityPerc,
        "onPriorityTime": onPriorityTime,
        "offPriorityTime": offPriorityTime,
        "onPrioritySeconds": onPrioritySeconds,
        "offPrioritySeconds": offPrioritySeconds,
        "convertedOnPriorityTime": convertedOnPriorityTime,
        "convertedOffPriorityTime": convertedOffPriorityTime,
        "allTimeTracked": allTimeTracked,
        "allTimeSeconds": allTimeSeconds,
        "allTimeOnPriorityTracked": allTimeOnPriorityTracked,
        "allTimeOffPriorityTracked": allTimeOffPriorityTracked,
        "onPriorityPercAllTime": onPriorityPercAllTime,
        "offPriorityPercAllTime": offPriorityPercAllTime
    }
    return render(request, 'actions/action_list.html', context)


# Internal Functions

def openActions(query):
    """
    Calculating the number of Open Actions.
    """
    openActions = Action.objects.filter(doneStatus=False, actionDate=query).count()
    return openActions


def completedActions(query):
    """
    Calculating the number of Completed Actions.
    """
    completedActions = Action.objects.filter(doneStatus=True, actionDate=query).count()
    return completedActions


def totalActions(query):
    """
    Calculating the number of Actions.
    """
    totalActions = Action.objects.filter(actionDate=query).count()
    return totalActions


def trackedTime(query):
    """
    Calculating the tracked time for the query date.
    """
    trackedTime = Action.objects.filter(actionDate=query).aggregate(Sum('trackedTime'))
    return trackedTime


def trackedSeconds(totalActionTime):
    """
    Converting trackedTime object into Seconds.
    """
    time_dict = totalActionTime
    time = time_dict.get("trackedTime__sum")
    if time == None:
        trackedSeconds = 0
    else:
        trackedSeconds = totalActionTime['trackedTime__sum'].total_seconds()
    return trackedSeconds


def trackedToday(totalSeconds):
    """
    Converting trackedSeconds into HH:MM:SS.
    """
    seconds = totalSeconds
    minutes = seconds // 60
    hours = minutes // 60
    trackedToday = "%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60)
    return trackedToday


def onPriorityActions(query):
    """
    Calculating the number of On Priority Actions.
    """
    onPriorityActions = Action.objects.filter(actionDate=query).exclude(priority__isnull=True).count()
    return onPriorityActions


def offPriorityActions(query):
    """
    Calculating the number of Off Priority Actions.
    """
    offPriorityActions = Action.objects.filter(actionDate=query).exclude(priority__isnull=False).count()
    return offPriorityActions


def onPriorityCalc(totalSeconds, onPrioritySeconds):
    """
    Calculating the % of On Priority Actions.
    """
    onPriorityCalc = (onPrioritySeconds * 100) / totalSeconds
    return onPriorityCalc


def offPriorityCalc(totalSeconds, offPrioritySeconds):
    """
    Calculating the % of Off Priority Actions.
    """
    offPriorityCalc = (offPrioritySeconds * 100) / totalSeconds
    return offPriorityCalc


def onPriorityTrackedTime(query):
    """
    Calculating the time tracked for On Priority Actions.
    """
    onPriorityTrackedTime = Action.objects.filter(actionDate=query).exclude(priority__isnull=True).aggregate(Sum('trackedTime'))
    return onPriorityTrackedTime


def offPriorityTrackedTime(query):
    """
    Calculating the time tracked for Off Priority Actions.
    """
    offPriorityTrackedTime = Action.objects.filter(actionDate=query).exclude(priority__isnull=False).aggregate(Sum('trackedTime'))
    return offPriorityTrackedTime


def trackedTimeAll(query):
    """
    Calculating the tracked time for all time.
    """
    trackedTimeAll = Action.objects.all().aggregate(Sum('trackedTime'))
    return trackedTimeAll


def onPriorityTrackedAllTime(query):
    """
    Calculating the time tracked for On Priority All Time.
    """
    onPriorityTrackedAllTime = Action.objects.all().exclude(priority__isnull=True).aggregate(Sum('trackedTime'))
    return onPriorityTrackedAllTime


def offPriorityTrackedAllTime(query):
    """
    Calculating the time tracked for Off Priority All Time.
    """
    offPriorityTrackedAllTime = Action.objects.all().exclude(priority__isnull=False).aggregate(Sum('trackedTime'))
    return offPriorityTrackedAllTime


@login_required(login_url='login')
def get_filtered_action_list(request):
    """
    Retrieves the filtered action_list template.
    """
    query_dict = request.GET
    query = query_dict.get("actionDate")
    actions = Action.objects.all()
    filteredActions = Action.objects.filter(actionDate=query)
    context = {
        "actions": actions,
        "query": query,
        "filteredActions": filteredActions
    }
    return render(request, 'actions/filtered_action_list.html', context)


@login_required(login_url='login')
def get_priorities_list(request):
    """
    Retrieves the priorities_list template.
    """
    priorities = Priority.objects.all()
    context = {
        "priorities": priorities
    }
    return render(request, 'actions/priorities_list.html', context)


@login_required(login_url='login')
def get_categories_list(request):
    """
    Retrieves the categories_list template.
    """
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'actions/categories_list.html', context)


@login_required(login_url='login')
def add_action(request):
    """
    Submits the ActionForm and Creates an Action
    """
    actionform = ActionForm()
    if request.method == "POST":
        actionform = ActionForm(request.POST)
        if actionform.is_valid():
            instance = actionform.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/actions/')

    context = {'actionform': actionform}
    return render(request, 'actions/add_action.html', context)


@login_required(login_url='login')
def complete_action(request, pk):
    """
    Submits the ActionForm and Updates an Action
    """
    actionform = ActionForm()
    action = Action.objects.get(id=pk)
    action.doneStatus = not action.doneStatus
    action.save()
    return redirect('/actions/')

    context = {'actionform': actionform}
    return render(request, 'actions/update_action.html', context)


@login_required(login_url='login')
def relist_action(request, pk):
    """
    Submits the ActionForm and Relists an Action
    """
    actionform = ActionForm()
    action = Action.objects.get(id=pk)
    action.actionDate = date.today()
    action.save()
    return redirect('/actions/')

    context = {'actionform': actionform}
    return render(request, 'actions/update_action.html', context)


@login_required(login_url='login')
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
            return redirect('/actions/')

    context = {'actionform': actionform}
    return render(request, 'actions/update_action.html', context)


@login_required(login_url='login')
def delete_action(request, pk):
    """
    Deletes the selected Action
    """
    action = Action.objects.get(id=pk)
    if request.method == "POST":
        action.delete()
        return redirect('/actions/')

    context = {'item': action}
    return render(request, 'actions/delete_action.html', context)


@login_required(login_url='login')
def add_category(request):
    """
    Submits the CategoryForm and Creates a Category
    """
    categoryform = CategoryForm()
    if request.method == "POST":
        categoryform = CategoryForm(request.POST)
        if categoryform.is_valid():
            instance = categoryform.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/categories/')

    context = {'categoryform': categoryform}
    return render(request, 'actions/add_category.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def add_priority(request):
    """
    Submits the PriorityForm and Creates a Priority
    """
    priorityform = PriorityForm()
    if request.method == "POST":
        priorityform = PriorityForm(request.POST)
        if priorityform.is_valid():
            instance = priorityform.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/priorities/')

    context = {'priorityform': priorityform}
    return render(request, 'actions/add_priority.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
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


def register_page(request):
    """
    Allows new user registrations
    """
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
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
    actionform = ActionForm()
    action = Action.objects.get(id=pk)
    action.trackedStart = datetime.datetime.now(timezone.utc)
    action.trackingStatus = True
    action.save()
    return redirect('/actions/')


@login_required(login_url='login')
def stop_timer(request, pk):
    """
    Submits the ActionForm and sets the start time for an Action
    """
    actionform = ActionForm()
    action = Action.objects.get(id=pk)
    action.trackingStatus = False
    action.trackedStop = datetime.datetime.now(timezone.utc)
    if action.activeTrackedTime is None:
        action.activeTrackedTime = action.trackedStop - action.trackedStart
        action.trackedTime = action.activeTrackedTime
    else:
        action.activeTrackedTime = action.trackedStop - action.trackedStart
        action.trackedTime = action.trackedTime + action.activeTrackedTime
    action.save()
    return redirect('/actions/')


@login_required(login_url='login')
def tracking_status(request, pk):
    """
    Submits the ActionForm and Updates an Action Tracking Status
    """
    actionform = ActionForm()
    action = Action.objects.get(id=pk)
    action.trackingStatus = not action.trackingStatus
    action.save()
    return redirect('/actions/')

