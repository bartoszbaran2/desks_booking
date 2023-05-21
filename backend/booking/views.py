from rest_framework.generics import ListAPIView, get_object_or_404, ListCreateAPIView

from . import serializers, models
from . import models


class DepartmentListView(ListAPIView):
    serializer_class = serializers.DepartmentSerializer
    queryset = models.Department.objects.all()


class DeskListView(ListAPIView):
    serializer_class = serializers.DeskSerializer
    queryset = models.Desk.objects.all()

    def get_queryset(self):
        department = get_object_or_404(models.Department, pk=self.kwargs.get("pk"))
        return models.Desk.objects.filter(department=department.id)


class EmployeeListView(ListCreateAPIView):
    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()

    def get_queryset(self):
        department = get_object_or_404(models.Department, pk=self.kwargs.get("pk"))
        return models.Employee.objects.filter(department=department.id)

    def perform_create(self, serializer):
        department = get_object_or_404(models.Department, pk=self.kwargs.get("pk"))
        serializer.save(department=department)
