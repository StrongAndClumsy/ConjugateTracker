from django.test import TestCase
from django.utils import timezone
from .models import *
from django.contrib.auth.models import User

# Create your tests here.

class TrackerViewsTestCase(TestCase):
    """ Test views to make sure we're displaying the proper content """

    def setUp(self):
        test_user1 = User.objects.create_user('test_user1', 'test@example.com', 'testpass1')
        test_user2 = User.objects.create_user('test_user2', 'test2@example.com', 'testpass2')
        self.test_bench1 = BenchMovement.objects.create(user=test_user1, created_at=timezone.now(), bar_type="dive", floor=True,
                                                        reverse=True, board=0, manpon=False, pin=False, bench_notes="None", bands_type="Some",
                                                        chain_weight=300, movement_weight=300, movement_sets=3, movement_reps=2, media_url="None")
        self.test_bench1.save()
        self.test_bench2 = BenchMovement.objects.create(user=test_user2, created_at=timezone.now(), bar_type="classy", floor=True,
                                                    reverse=True, board=False, manpon=False, pin=False, bench_notes="None", bands_type="Some", chain_weight=300)
        self.test_bench2.save()

    def test_index_when_logged_in(self):
        self.client.login(username='test_user1', password='testpass1')
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_user_can_access_own_content(self):
        self.client.login(username='test_user1', password='testpass1')
        resp = self.client.get('/bench_movement/%s/' % self.test_bench1.pk)
        self.assertEqual(resp.status_code, 200)

    def test_user_cannot_access_other_user_content(self):
        self.client.login(username='test_user1', password='testpass1')
        resp = self.client.get('/bench_movement/%s/' % self.test_bench2.pk)
        self.assertEqual(resp.status_code, 404)

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
