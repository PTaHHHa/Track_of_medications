from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, UpdateView
from django.db.models import Q
from .models import Patient
from .forms import UpdateForm


class HomeView(TemplateView):
    template_name = 'index.html'


class SearchView(ListView):
    model = Patient
    template_name = 'search_results.html'

    def get_queryset(self):
        first_name = self.request.GET.get('search_first_name')
        last_name = self.request.GET.get('search_last_name')
        search_result = Patient.objects.filter(Q(first_name__contains=first_name)
                                               & Q(last_name__contains=last_name))
        if not search_result:
            messages.error(self.request, 'Такого пациента нет')
        return search_result


class Update(UpdateView):
    model = Patient
    template_name = 'patient_form.html'
    form_class = UpdateForm
    success_url = '/'

    def get_object(self, queryset=None, *args, **kwargs):
        q = get_object_or_404(Patient, pk=self.kwargs['pk'])
        return q


