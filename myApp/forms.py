from django import forms
from django.contrib import admin
from .models import Patient


class SearchForm(forms.ModelForm):
    first_name = forms.CharField(max_length=90)
    last_name = forms.CharField(max_length=90)


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('last_name', 'first_name', 'middle_name', 'birth_date', 'medication')
        widgets = {
            'first_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'last_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'middle_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'birth_date': forms.DateInput(format='%d.%m.%Y', attrs={'readonly': 'readonly'}),
        }
        labels = {
            'medication': 'medication',
        }


class StatsModelAdmin(admin.ModelAdmin):
    readonly_fields = ('type_1', 'type_2', 'type_3', 'type_4', 'type_5',)




