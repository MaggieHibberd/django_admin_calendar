from __future__ import unicode_literals

from django.contrib import admin
from .models import Course
admin.site.register(Course)

# ======================================================================================================================


class CourseAdmin(admin.ModelAdmin):
    search_fields = 'name'
    list_display = ['name', ]
    fields = ('name', )
