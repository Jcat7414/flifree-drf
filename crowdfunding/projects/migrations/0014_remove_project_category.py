# Generated by Django 3.0.8 on 2020-09-22 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20200917_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
    ]
