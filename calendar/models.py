from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime


# ===================================================================================================================


class Course(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, unique=True, help_text=u'Course name',
                            verbose_name="course_name")
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True, unique=False, help_text=u'Course description',
                                   verbose_name="description")

    class Meta:
        db_table = "courses"

    def __str__(self):
        return self.name

# ===================================================================================================================


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False, unique=False, help_text=u'First name',
                                  verbose_name="first_name")
    last_name = models.CharField(max_length=100, null=False, blank=False, unique=False, help_text=u'Last name',
                                 verbose_name="last_name")
    date = models.DateTimeField(default=datetime.now, blank=True)
    courses = models.ManyToManyField(Course)

    class Meta:
        db_table = "students"
        unique_together = (("first_name", "last_name"),)

    def __str__(self):
        return self.first_name, self.last_name, self.courses

    def clean(self):
        if self.pk is None and Student.objects.filter(first_name=self.first_name,
                                                      last_name=self.last_name).exists():
            raise ValidationError("A person with the same first and last name already exists!")

# ===================================================================================================================


class Event(models.Model):
    day = models.DateField(u'Date of event', help_text=u'Day of the event')
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Finish time', help_text=u'Finish time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'
        db_table = "events"

    def __str__(self):
        return self.day, self.student, self.course




