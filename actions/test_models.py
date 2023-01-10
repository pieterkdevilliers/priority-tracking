from django.test import TestCase
from .models import Action

# Create your tests here.

class TestMoodels(TestCase):
    """
    Testing Models
    """
    def test_this_thing_works(self):
        """
        All Actions are created with done_status as Not Done by default
        """
        action = Action.objects.create(title='Test default done status')
        self.assertFalse(action.done_status)