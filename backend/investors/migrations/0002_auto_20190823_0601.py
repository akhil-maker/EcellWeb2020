# Generated by Django 2.2.2 on 2019-08-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='social_media',
            field=models.URLField(),
        ),
    ]
