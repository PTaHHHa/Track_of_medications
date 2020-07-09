from django import forms
from django.contrib import admin
from .models import Patient


class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('type_1', 'type_2', 'type_3', 'type_4', 'type_5',)


class SearchForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name')
