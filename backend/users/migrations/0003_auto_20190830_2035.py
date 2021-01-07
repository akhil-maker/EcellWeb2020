# Generated by Django 2.2.2 on 2019-08-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190818_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('GST', 'Guest'), ('VLT', 'Voluteer'), ('EXE', 'Executive'), ('MNG', 'Manager'), ('HCO', 'Head Co-ordinator'), ('OCO', 'Overall Co-ordinator'), ('CAB', 'Campus Ambassador'), ('STO', 'Startup Owner'), ('DRT', 'Director')], default='GST', max_length=3),
        ),
    ]
