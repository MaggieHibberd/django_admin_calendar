# Generated by Django 4.1.7 on 2023-04-02 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Course name', max_length=30, unique=True, verbose_name='course_name')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.CharField(blank=True, help_text='Course description', max_length=300, null=True, verbose_name='description')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
