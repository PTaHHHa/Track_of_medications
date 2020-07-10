from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from .models import Patient, Stats
from django.contrib.auth.models import Group
from .forms import StatsModelAdmin


class ArrayModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


admin.site.unregister(Group)
admin.site.register(Patient, ArrayModelAdmin)
admin.site.register(Stats, StatsModelAdmin)
