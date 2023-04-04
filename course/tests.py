import unittest

from django.test import TestCase
from .models import Course


class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(name="Computer Science", description="It's programming and shizzle innit")
        Course.objects.create(name="City & Guilds - Painting and Decorating", description="Get on the painting and "
                                                                                          "decorating flex!")

    def test_get_my_course(self):
        """Animals that can speak are correctly identified"""
        cs = Course.objects.get(name="Computer Science")
        pd = Course.objects.get(name="City & Guilds - Painting and Decorating")
        self.assertEqual(cs.name(), "Computer Science")
        self.assertEqual(pd.name(), "City & Guilds - Painting and Decorating")


if __name__ == '__main__':
    unittest.main()