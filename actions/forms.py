from django.forms import ModelForm
from .models import Action, Priority, Category


class ActionForm(ModelForm):
    class Meta:
        model = Action
        fields = ['title', 'priority', 'category']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = '__all__'
