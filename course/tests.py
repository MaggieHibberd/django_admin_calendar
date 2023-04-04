from django.test import TestCase
from .models import Course


class CourseTestCase(TestCase):
    print('Setting up Course model tests')

    def setUp(self):
        Course.objects.create(name="Computer Science", description="It's programming and shizzle innit")
        Course.objects.create(name="City & Guilds - Painting and Decorating", description="Get on the painting and "
                                                                                          "decorating flex!")

    def test_course_one(self):
        course = Course.objects.get(id=1)
        expected_object_name = f'{course.name}'
        expected_object_desi = f'{course.description}'
        self.assertEqual((course is not None) and str(course.name), expected_object_name)
        self.assertEqual((course is not None) and str(course.description), expected_object_desi)

    def test_course_two(self):
        course = Course.objects.get(id=2)
        expected_object_name = f'{course.name}'
        expected_object_desi = f'{course.description}'
        self.assertEqual((course is not None) and str(course), expected_object_name)
        self.assertEqual((course is not None) and str(course.description), expected_object_desi)


print('Course model tests ended')
