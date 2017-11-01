from django.test import TestCase
from coderdojochi.models import Course


class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(title="HTML")

    # def test_course_title(self):
    #     """Courses that can speak are correctly identified"""
    #     html = Course.objects.get(title="HTML")
    #     self.assertEqual(html.speak(), 'The lion says "roar"')
    #     self.assertEqual(cat.speak(), 'The cat says "meow"')
