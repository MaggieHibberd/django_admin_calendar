from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime
from course.models import Course

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