"""priority_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from actions.views import get_action_list, get_priorities_list,\
    get_categories_list, add_action, add_category, add_priority,\
    update_action, update_category, update_priority, delete_action,\
    delete_category, delete_priority

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_action_list, name='get_action_list'),
    path('priorities/', get_priorities_list, name='get_priorities_list'),
    path('categories/', get_categories_list, name='get_categories_list'),
    path('add-action/', add_action, name='add_action'),
    path('add-category/', add_category, name='add_category'),
    path('add-priority/', add_priority, name='add_priority'),
    path('add-new-action/', add_action, name='add_new_action'),
    path('add-new-category/', add_category, name='add_new_category'),
    path('add-new-priority/', add_priority, name='add_new_priority'),
    path('update-action/<str:pk>/', update_action, name='update_action'),
    path('update-priority/<str:pk>/', update_priority, name='update_priority'),
    path('update-category/<str:pk>/', update_category, name='update_category'),
    path('delete-action/<str:pk>/', delete_action, name='delete_action'),
    path('delete-category/<str:pk>/', delete_category, name='delete_category'),
    path('delete-priority/<str:pk>/', delete_priority, name='delete_priority'),
]
