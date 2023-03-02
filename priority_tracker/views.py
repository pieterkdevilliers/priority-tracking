"""
Global views
"""

from django.shortcuts import render


def handler400(request, exception):
    """
    Custom error handler for 400 errors
    """
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    context = {
        "username": username,
        "user_id": user_id,
    }
    return render(request, 'actions/400.html', context, status=400)


def handler403(request, exception):
    """
    Custom error handler for 403 errors
    """
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    context = {
        "username": username,
        "user_id": user_id,
    }
    return render(request, 'actions/403.html', context, status=403)


def handler404(request, exception):
    """
    Custom error handler for 404 errors
    """
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    context = {
        "username": username,
        "user_id": user_id,
    }
    return render(request, 'actions/404.html', context, status=404)


def handler500(request):
    """
    Custom error handler for 500 errors
    """
    current_user = request.user
    user_id = current_user.id
    username = current_user.username
    context = {
        "username": username,
        "user_id": user_id,
    }
    return render(request, 'actions/500.html', context, status=500)
