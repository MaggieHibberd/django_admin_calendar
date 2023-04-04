from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime
from course.models import Course
from student.models import Student


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
        return '{} {} {}'.format(self.day, self.student, self.course)




