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
