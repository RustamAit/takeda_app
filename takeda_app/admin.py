from django.contrib import admin

# Register your models here.
from takeda_app.models import Worker, Department, Position, Mark

admin.site.register(Worker)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Mark)