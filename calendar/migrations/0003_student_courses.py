# Generated by Django 4.1.7 on 2023-04-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='calendar.course'),
        ),
    ]
