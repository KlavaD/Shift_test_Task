from django.contrib import admin

from .models import Salary


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = (
        'worker',
        'date_of_increase',
        'sum_of_salary',
        'next_date_of_increase',
        'is_actual'
    )
    list_filter = ('worker',)
    search_fields = (
        'worker',
        'date_of_increase',
        'next_date_of_increase'
    )
