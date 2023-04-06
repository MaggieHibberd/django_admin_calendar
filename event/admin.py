from __future__ import unicode_literals

from django.contrib import admin
from .models import Event
from course.models import Course
from student.models import Student
admin.site.register(Event)


# ======================================================================================================================
# class StudentInline(admin.TabularInline):
#     model = Student
#     fields = ('id', 'first_name', 'last_name')
#     readonly_fields = ('id', )
#     extra = 0


class EventAdmin(admin.ModelAdmin):

    list_display = ['event__student__id', 'day', 'start_time', 'end_time', 'notes', ]

    fields = (
        'day',
        'start_time',
        'end_time',
        'notes',
            )
    # inlines = (StudentInline,)

    # ------------------------------------------------------------------------------------------------------------------
    # def get_student_name(self, obj: Student) -> str:
    #     result = f'{obj.first_name, obj.last_name}'
    #     return result
    #
    # get_student_name.short_description = 'Student'


