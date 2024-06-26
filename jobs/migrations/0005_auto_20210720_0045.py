# Generated by Django 3.2.5 on 2021-07-19 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_project_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='assigned',
        ),
        migrations.RemoveField(
            model_name='project',
            name='responsible',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='projectName',
        ),
        migrations.CreateModel(
            name='ProjectHandle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.employee')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.project')),
            ],
        ),
        migrations.AddField(
            model_name='tracker',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.projecthandle'),
        ),
    ]
