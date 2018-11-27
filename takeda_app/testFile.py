from takeda_app.models import Position

for i in Position.objects.all():
    print(i.title)