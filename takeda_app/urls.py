
from django.urls import path, include
from rest_framework import routers

from takeda_app import views

router = routers.DefaultRouter()
router.register('workers', views.WorkerList)
router.register('events', views.EventList)
router.register('tasks', views.ActiveTaskList)
router.register('projects', views.ActiveProjectList)
router.register('department_tasks/', views.DepartmentTaskList)
router.register('departments/', views. DepartmentList)
router.register('positions/',views.PositionList)



urlpatterns = [
    path('', include(router.urls)),
]
