from rest_framework.generics import ListAPIView, get_object_or_404

from . import serializers, models
from . import models


class DepartmentListView(ListAPIView):
    serializer_class = serializers.DepartmentSerializer
    queryset = models.Department.objects.all()


class DeskListView(ListAPIView):
    serializer_class = serializers.DeskSerializer
    queryset = models.Desk.objects.all()

    def get_queryset(self):
        department = get_object_or_404(queryset=models.Department.objects.all(), pk=self.kwargs.get("pk"))
        return models.Desk.objects.filter(department=department.id)
