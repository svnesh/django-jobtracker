# Generated by Django 3.2.5 on 2022-10-24 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_remove_employee_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='workedDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
