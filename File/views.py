from django.shortcuts import render
from .models import File


# Create your views here.
def index(requests):
    context = {
        'files': File.objects.all(),
    }
    return render(requests, 'index.html', context)
