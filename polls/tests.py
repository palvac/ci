from django.test import TestCase

from polls.models import Poll


class TestModels(TestCase):
    def test_poll_created(self):
        Poll.objects.create(name="Subaru Forester SG5 Poll")
        self.assertEqual(Poll.objects.count(), 1)
