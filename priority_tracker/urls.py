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
from actions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_page, name='login'),
    path('', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register'),
    path('actions/', views.get_action_list, name='get_action_list'),
    path('filtered-actions/', views.get_filtered_action_list, name='get_filtered_action_list'),
    path('priorities/', views.get_priorities_list, name='get_priorities_list'),
    path('categories/', views.get_categories_list, name='get_categories_list'),
    path('add-action/', views.add_action, name='add_action'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-priority/', views.add_priority, name='add_priority'),
    path('add-new-action/', views.add_action, name='add_new_action'),
    path('add-new-category/', views.add_category, name='add_new_category'),
    path('add-new-priority/', views.add_priority, name='add_new_priority'),
    path('update-action/<str:pk>/', views.update_action, name='update_action'),
    path('relist-action/<str:pk>/', views.relist_action, name='relist_action'),
    path('update-priority/<str:pk>/', views.update_priority, name='update_priority'),
    path('update-category/<str:pk>/', views.update_category, name='update_category'),
    path('delete-action/<str:pk>/', views.delete_action, name='delete_action'),
    path('delete-category/<str:pk>/', views.delete_category, name='delete_category'),
    path('delete-priority/<str:pk>/', views.delete_priority, name='delete_priority'),
    path('complete-action/<str:pk>/', views.complete_action, name='complete_action'),
    path('start-timer/<str:pk>/', views.start_timer, name='start_timer'),
    path('stop-timer/<str:pk>/', views.stop_timer, name='stop_timer'),
    path('tracking-status/<str:pk>/', views.tracking_status, name='tracking_status'),
    path('priority_active_status/<str:pk>/', views.priority_active_status, name='priority_active_status'),
    path('complete-filtered-action/<str:pk>/', views.complete_filtered_action, name='complete_filtered_action'),
]
