from django.db import models

# Create your models here.


class Worker(models.Model):
    email = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=60, default='111')
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=70)
    department = models.ForeignKey('Department', on_delete= models.PROTECT)
    position = models.ForeignKey('Position', on_delete= models.PROTECT)
    marks = models.ManyToManyField('Mark')
    tasks_created = models.ManyToManyField('Task')

    def get_rating(self):
        rating = 0
        for i in self.marks.all():
            rating += i.mark
        return rating/self.marks.all()


class Department(models.Model):
    title = models.CharField(max_length=60)


class Position(models.Model):
    title = models.CharField(max_length=60)
    salary = models.IntegerField()
    department = models.ForeignKey('Department',on_delete=models.CASCADE)


class Mark(models.Model):
    mark = models.FloatField(default=0.0)
    task = models.ForeignKey('Task', on_delete=models.PROTECT )


class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    department = models.ForeignKey("Department", on_delete=models.PROTECT)
    deadline = models.DateTimeField(default='2019-01-01 00:00:00')
    executor = models.ManyToManyField("Worker")

    def mark_executor(self,mt: float,executorId: int):
        m = Mark(mark = mt,task = self.id)
        m.save()
        self.executor.get(id = executorId).marks.add(m)


class Project(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    department = models.ForeignKey("Department", on_delete=models.PROTECT)
    # deadline = models.DateTimeField(default='2019-01-01 00:00:00')
    sub_tasks = models.ManyToManyField('Task')
    executors = models.ManyToManyField('Worker')


class Event(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(default='2019-01-01 00:00:00')
    participants = models.ManyToManyField('Worker')
