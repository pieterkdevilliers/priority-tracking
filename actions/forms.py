"""
ModelForms for Actions App
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Action, Priority, Category

User = get_user_model()

class ActionForm(ModelForm):
    """
    ModelForm for adding Actions
    """
    class Meta:
        """
        Meta class for ActionForm
        """
        model = Action
        fields = ['title', 'priority', 'category']


class CategoryForm(ModelForm):
    """
    ModelForm for adding Categories
    """
    class Meta:
        """
        Meta class for CategoryForm
        """
        model = Category
        fields = ['title', 'description']


class PriorityForm(ModelForm):
    """
    ModelForm for adding Priorities
    """
    class Meta:
        """
        Meta class for PriorityForm
        """
        model = Priority
        fields = ['title', 'description', 'category', 'activeStatus']


class CreateUserForm(UserCreationForm):
    """
    ModelForm for User Registration
    """
    class Meta:
        """
        Meta class for CreateUserForm
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
