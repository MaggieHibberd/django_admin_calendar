import unittest
from django.test import TestCase
from .models import Course


class TestCourse(TestCase):

    def test_string_representation(self):
        course = Course(name="Test Course")
        self.assertEqual(str(course), course.name)


if __name__ == '__main__':
    unittest.main()
