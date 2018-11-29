from django.shortcuts import render
from .models import Board

# remove
from django.http import HttpResponse

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
