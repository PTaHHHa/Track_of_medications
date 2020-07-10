from django import forms
from django.contrib import admin
from .models import Patient
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class SearchForm(forms.ModelForm):
    first_name = forms.CharField(max_length=90)
    last_name = forms.CharField(max_length=90)


# class PatientModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
#     class Meta:
#         model = Patient


class StatsModelAdmin(admin.ModelAdmin):
    readonly_fields = ('type_1', 'type_2', 'type_3', 'type_4', 'type_5',)

# class SearchForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = ('first_name', 'last_name')
