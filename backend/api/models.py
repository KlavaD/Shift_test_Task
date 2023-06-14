from django.db import models

from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint

User = get_user_model()


class Salary(models.Model):
    sum_of_salary = models.PositiveIntegerField(
        verbose_name='Сумма',
        null=False,
    )
    date_of_increase = models.DateField(
        verbose_name='Дата повышения',
        auto_now_add=True
    )
    next_date_of_increase = models.DateField(
        verbose_name='Следующее повышение',
        null=False,
    )
    worker = models.ForeignKey(
        User,
        verbose_name='Работник',
        on_delete=models.CASCADE,
        related_name='salary'
    )
    is_actual = models.BooleanField(
        verbose_name='актуальность зп',
        default=True,
    )

    class Meta:
        verbose_name = 'Зарплата'
        verbose_name_plural = 'Список зарплат'
        ordering = ('-date_of_increase',)


    def __str__(self):
        return (f'(Зарплата - {self.sum_of_salary}.)'
                f'(Следующее повышение - {self.next_date_of_increase})')
