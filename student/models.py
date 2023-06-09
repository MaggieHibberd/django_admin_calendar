from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
import django
from course.models import Course
from django.utils import timezone

# ===================================================================================================================


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False, unique=False, help_text=u'First name',
                                  verbose_name="first_name")
    last_name = models.CharField(max_length=100, null=False, blank=False, unique=False, help_text=u'Last name',
                                 verbose_name="last_name")
    date = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    courses = models.ManyToManyField(Course)

    class Meta:
        db_table = "students"

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def clean(self):
        if self.pk is None and Student.objects.filter(first_name=self.first_name,
                                                      last_name=self.last_name).exists():
            raise ValidationError("A person with the same first and last name already exists!")