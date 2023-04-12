from __future__ import unicode_literals

from django.contrib import admin
from .models import Student
from course.models import Course

# ======================================================================================================================


class CourseInline(admin.TabularInline):
    model = Student.courses.through
    list_display = ['name', ]

# ======================================================================================================================

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', ]
    exclude = ['courses']
    inlines = [CourseInline, ]


