# Generated by Django 3.2.5 on 2021-08-17 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_alter_employee_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='fileCount',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='spentTimeHr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='spentTimeMin',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]