from django.test import TestCase
from .models import Student
from course.models import Course


class StudentTestCase(TestCase):
    print('Setting up Student model tests')

    def setUp(self):
        course = Course.objects.create(name="Computer Science", description="It's programming and shizzle innit")
        student = Student.objects.create(first_name="Stu", last_name="Dent")
        student.courses.add(course)

    def test_student(self):
        student = Student.objects.get(id=1)
        expected_object_firstname = f'{student.first_name}'
        expected_object_lastname = f'{student.last_name}'
        expected_object_course = f'{student.courses}'
        self.assertEqual((student is not None) and str(student.first_name), expected_object_firstname)
        self.assertEqual((student is not None) and str(student.last_name), expected_object_lastname)
        self.assertEqual((student is not None) and str(student.courses), expected_object_course)


print('Student model tests ended')

