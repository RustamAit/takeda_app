# Generated by Django 2.1.3 on 2018-11-25 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('takeda_app', '0003_position_deparmnent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='deparmnent',
            new_name='department',
        ),
    ]