from django.shortcuts import render
from .forms import SearchForm
from .models import Patient
from django.views.generic import ListView, TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'


class SearchView(ListView):
    model = Patient
    template_name = 'search_results.html'

    def get_queryset(self):
        q = Patient.objects.filter(first_name='Владимир', last_name='Путин')
        return q


