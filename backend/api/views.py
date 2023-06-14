from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Salary, User
from .permissions import IsAuthorOnly, IsAdminOnly
from .serializers import SalarySerializer, PostSalarySerializer


class SalaryViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return PostSalarySerializer
        return SalarySerializer

    def get_permission_classes(self):
        if self.request.method in ['GET']:
            return IsAuthorOnly
        return IsAdminOnly

    def get_queryset(self):
        return Salary.objects.filter(worker=self.request.user.pk,
                                     is_actual=True)

    def create(self, request, *args, **kwargs):
        active_salary = Salary.objects.filter(
            worker=get_object_or_404(
                User, username=request.data.get('worker')
            ),
            is_actual=True,
        )
        if active_salary:
            active_salary = active_salary.get()
            active_salary.is_actual = 0
            active_salary.save()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)
