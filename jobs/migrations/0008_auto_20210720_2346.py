# Generated by Django 3.2.5 on 2021-07-20 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20210720_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='handled',
            field=models.ManyToManyField(to='jobs.Employee'),
        ),
        migrations.DeleteModel(
            name='ProjectHandle',
        ),
    ]
