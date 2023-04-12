from __future__ import unicode_literals

import datetime
from calendar import calendar, HTMLCalendar
import calendar
from .utils import EventCalendar
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from events.models import Event
# from course.models import Course
# from student.models import Student


# ======================================================================================================================
# class StudentInline(admin.TabularInline):
#     model = Student
#     fields = ('id', 'first_name', 'last_name')
#     readonly_fields = ('id', )
#     extra = 0
# ======================================================================================================================

class EventAdmin(admin.ModelAdmin):

    list_display = ['course', 'student', 'day', 'start_time', 'end_time', 'notes', ]

    fields = (
        'student',
        'course',
        'day',
        'start_time',
        'end_time',
        'notes',
            )
    # inlines = (StudentInline,)

    # ------------------------------------------------------------------------------------------------------------------

    def changelist_view(self, request, extra_context=None):
        after_day = request.GET.get('day__gte', None)
        extra_context = extra_context or {}

        if not after_day:
            d = datetime.date.today()
        else:
            try:
                split_after_day = after_day.split('-')
                d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
            except:
                d = datetime.date.today()

        previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
        previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
        previous_month = datetime.date(year=previous_month.year, month=previous_month.month,
                                       day=1)  # find first day of previous month

        last_day = calendar.monthrange(d.year, d.month)
        next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
        next_month = next_month + datetime.timedelta(days=1)  # forward a single day
        next_month = datetime.date(year=next_month.year, month=next_month.month,
                                   day=1)  # find first day of next month

        extra_context['previous_month'] = reverse('admin:events_event_changelist') + '?day__gte=' + str(
            previous_month)
        extra_context['next_month'] = reverse('admin:events_event_changelist') + '?day__gte=' + str(next_month)

        cal = EventCalendar()
        html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
        html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')
        extra_context['calendar'] = mark_safe(html_calendar)
        return super(EventAdmin, self).changelist_view(request, extra_context)

# ======================================================================================================================


class EventList(Event):
    class Meta:
        proxy = True

# ======================================================================================================================


class EventListAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'day', 'start_time', 'end_time', 'notes', ]

# ======================================================================================================================


admin.site.register(EventList, EventListAdmin)
admin.site.register(Event, EventAdmin)



