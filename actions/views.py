from django.shortcuts import render


# Create your views here.

def get_action_list(request):
    return render(request, 'actions/action_list.html')
