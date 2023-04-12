from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime

from django.urls import reverse

from course.models import Course
from student.models import Student

# ======================================================================================================================


class Event(models.Model):
    day = models.DateField(u'Date of events', help_text=u'Day of the events')
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, null=False)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, null=False)
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Finish time', help_text=u'Finish time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'
        db_table = "events"

    # ------------------------------------------------------------------------------------------------------------------
    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  # edge case
            overlap = False
        elif (fixed_start <= new_start <= fixed_end) or (
                fixed_start <= new_end <= fixed_end):  # inner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
            overlap = True

        return overlap

    # ------------------------------------------------------------------------------------------------------------------
    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another events: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))

    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        return '|| DATE:{} || STUDENT:{} {}  || COURSE:{}  ||'.format(self.day, self.student.first_name,
                                                                      self.student.last_name, self.course.name)




