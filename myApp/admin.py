from django.contrib import admin
from .models import Patient, Stats
from django.contrib.auth.models import Group
from .forms import MyModelAdmin


admin.site.unregister(Group)
admin.site.register(Patient)
admin.site.register(Stats, MyModelAdmin)
