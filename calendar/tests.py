from django.test import TestCase
from student.models import Student
from course.models import Course
from .models import Event


class EventTestCase(TestCase):
    print('Setting up Event model tests')

    def setUp(self):
        course = Course.objects.create(name="Computer Science", description="It's programming and shizzle innit")
        student = Student.objects.create(first_name="Stu", last_name="Dent")
        student.courses.add(course)
        Event.objects.create(day='2010-10-01', start_time='13:00:00', end_time='14:00:00', notes='NOTED!',
                             course=course, student=student)

    def test_student(self):
        event_ob = Event.objects.get(id=1)
        expected_object_day = f'{event_ob.day}'
        expected_object_start = f'{event_ob.start_time}'
        expected_object_end = f'{event_ob.end_time}'
        expected_object_notes = f'{event_ob.notes}'
        expected_object_course = f'{event_ob.course}'
        expected_object_student = f'{event_ob.student}'
        self.assertEqual((event_ob is not None) and str(event_ob.day), expected_object_day)
        self.assertEqual((event_ob is not None) and str(event_ob.start_time), expected_object_start)
        self.assertEqual((event_ob is not None) and str(event_ob.end_time), expected_object_end)
        self.assertEqual((event_ob is not None) and str(event_ob.notes), expected_object_notes)
        self.assertEqual((event_ob is not None) and str(event_ob.course), expected_object_course)
        self.assertEqual((event_ob is not None) and str(event_ob.student), expected_object_student)


print('Event model tests ended')

