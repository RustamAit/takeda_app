from rest_framework import serializers
from takeda_app.models import *


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'title', 'salary')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'title')


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ('id', 'mark')


class WorkerSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False, read_only=True)
    position = PositionSerializer(many=False, read_only=True)

    class Meta:
        model = Worker
        fields = ('id', 'name', 'surname', 'department','position','email','password')


class TaskSerializer(serializers.ModelSerializer):
    executor = WorkerSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'department','deadline','executor')


class ProjectSerializer(serializers.ModelSerializer):
    executors = WorkerSerializer(many=True, read_only=True)
    sub_tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'status', 'department','sub_tasks','executors')


class EventSerializer(serializers.ModelSerializer):
    participants = WorkerSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date', 'participants')



