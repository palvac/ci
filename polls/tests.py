from django.test import TestCase

from polls.models import Poll


class TestModels(TestCase):
    def test_poll_created(self):
        Poll.objects.create(name="Subaru Forester SG5 Poll")
        self.assertEqual(Poll.objects.count(), 1)

    def test_circle_ci_execution(self):
        self.assertEqual("Circle CI Rocks!", "Circle CI Rocks!")

    def test_status_check_reporting(self):
        self.assertEqual("Status check Okay!", "Status check Okay!")
