from rest_framework import serializers

from api.models import Salary, User


class SalarySerializer(serializers.ModelSerializer):
    worker = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Salary
        fields = ('worker', 'sum_of_salary', 'next_date_of_increase')


class PostSalarySerializer(serializers.ModelSerializer):
    worker = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = Salary
        fields = ('worker', 'sum_of_salary', 'next_date_of_increase',)
