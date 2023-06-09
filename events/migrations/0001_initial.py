# Generated by Django 4.2 on 2023-04-05 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(help_text='Day of the events', verbose_name='Date of events')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='Starting time')),
                ('end_time', models.TimeField(help_text='Finish time', verbose_name='Finish time')),
                ('notes', models.TextField(blank=True, help_text='Textual Notes', null=True, verbose_name='Textual Notes')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
                'db_table': 'events',
            },
        ),
    ]
