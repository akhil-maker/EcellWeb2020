# Generated by Django 2.2.2 on 2020-04-17 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iportal', '0007_auto_20200415_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startup',
            name='approved',
        ),
    ]
