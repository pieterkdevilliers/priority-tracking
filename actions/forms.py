"""
ModelForms for Actions App
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
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
        fields = ['title', 'priority']

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'priority': forms.Select(attrs={'class': 'form-control'}),
            }


class UpdateActionForm(ModelForm):
    """
    ModelForm for Updating Actions
    """
    class Meta:
        """
        Meta class for UpdateActionForm
        """
        model = Action
        fields = ['title', 'priority', 'category']

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'priority': forms.Select(attrs={'class': 'form-control'}),
                'category': forms.Select(attrs={'class': 'form-control'}),
            }




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

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
            }


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

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
                'category': forms.Select(attrs={'class': 'form-control'}),
                'activeStatus': forms.CheckboxInput(attrs={'class': 'form-control form-check-input'}),
            }


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
