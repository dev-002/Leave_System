# Generated by Django 3.2.25 on 2024-04-05 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveSystem', '0002_applicationmodel_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='status',
            field=models.IntegerField(),
        ),
    ]