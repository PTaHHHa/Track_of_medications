from django.shortcuts import render
from .forms import SearchForm
# Create your views here.


def index(request):
    return render(request, '../templates/index.html')


def search_results(request):
    return render(request, '../templates/search_results.html')
