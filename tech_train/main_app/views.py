from django.shortcuts import render
from .models import Business  # Import your Business model here

def index(request):
    # Assuming you have a queryset of Business objects
    businesses = Business.objects.all()  # Or filter as needed
    return render(request, 'home.html', {'businesses': businesses})

