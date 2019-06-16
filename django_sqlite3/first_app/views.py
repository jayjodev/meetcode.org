from django.shortcuts import render
from .models import first_model, second_model, third_model

def home(request):

    context ={
        'first_models': first_model.objects.all(), # first_model in database
        'second_models': second_model.objects.all(), # second_model in database
        'third_models': third_model.objects.all()  # third in database
    }
    return render(request, 'first_app/home.html', context)
