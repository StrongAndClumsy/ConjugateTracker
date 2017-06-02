from django.test import TestCase
from django.utils import timezone
from .models import SquatMovement
from django.contrib.auth.models import User

# Create your tests here.
class SquatMovementTestCase(TestCase):
    def setUp(self):
        test_user= User.objects.create_user('test', 'test@example.com', 'testpass')
        SquatMovement.objects.create(user=test_user, created_at=timezone.now(),
                                        effort_type="dynamic", box_free="box",
                                        bar_type="test_heavy", bands_type="springy",
                                        chain_weight=200, movement_weight=150,
                                        movement_reps=10, squat_notes='notes for squat')

    def test_squats_can_save(self):
        """We can save squats"""
        test_squat = SquatMovement.objects.get(bar_type="test_heavy")
        self.assertEqual(test_squat.effort_type, 'dynamic')
