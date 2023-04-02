from __future__ import unicode_literals

from django.db import models


class Events(models.Model):
    day = models.DateField(u'Date of event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Finish time', help_text=u'Finish time')


