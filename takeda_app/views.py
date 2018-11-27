from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, status
from takeda_app.models import *
from takeda_app.serializers import *
from takeda_app import constants


class DepartmentList(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionList(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class WorkerList(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class ActiveTaskList(viewsets.ModelViewSet):
    queryset = Task.objects.filter(status = constants.IN_PROGRESS)
    serializer_class = TaskSerializer


class ActiveProjectList(viewsets.ModelViewSet):
    queryset = Project.objects.filter(status = constants.IN_PROGRESS)
    serializer_class = ProjectSerializer


class EventList(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer



class DepartmentTaskList(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.filter(department = Department.objects.get(title = "Finance"))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        req = self.request
        departmentId = req.query_params.get('id')
        if departmentId:
            self.queryset = Task.objects.filter(department = Department.objects.get(id = departmentId))
            return self.queryset
        else:
            return self.queryset


