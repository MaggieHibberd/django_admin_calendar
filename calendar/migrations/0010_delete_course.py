# Generated by Django 4.1.7 on 2023-04-03 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar', '0009_delete_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]