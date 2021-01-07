# Generated by Django 2.2.2 on 2019-08-17 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190817_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeboard',
            name='description',
            field=models.TextField(blank=True, default='afdadf'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='noticeboard',
            name='url',
            field=models.URLField(blank=True, default='https://www.youtube.com/results?search_query=django'),
            preserve_default=False,
        ),
    ]
