from django.db import models
from django.utils import timezone

# Create your models here.
class SquatMovement(models.Model):
	user = models.ForeignKey('auth.User')
	created_at = models.DateTimeField(default=timezone.now)
	effort_type = models.CharField(max_length=60)
	squat_notes = models.CharField(max_length=300,blank=True)
	box_free = models.CharField(max_length=60)
	bar_type = models.CharField(max_length=60, blank=True)
	bands_type = models.CharField(max_length=60, blank=True)
	chain_weight = models.IntegerField(default=0, blank=True)
	movement_weight = models.IntegerField(default=0)
	movement_reps = models.IntegerField(default=0)




class DeadliftMovement(models.Model):
	user = models.ForeignKey('auth.User')
	created_at = models.DateTimeField(default=timezone.now)
	sumo_conventional = models.CharField(max_length=60)
	deficit = models.BooleanField()
	block = models.BooleanField()
	standard = models.BooleanField()
	pin = models.BooleanField()
	reverse = models.BooleanField()
	movement_weight = models.IntegerField(default=0)
	movement_reps = models.IntegerField(default=0)
	deadlift_notes = models.CharField(max_length=60, blank=True)

class BenchMovement(models.Model):
	user = models.ForeignKey('auth.User')
	created_at = models.DateTimeField(default=timezone.now)
	bar_type = models.CharField(max_length=60, blank=True)
	floor = models.BooleanField()
	reverse = models.BooleanField()
	standard = models.BooleanField()
	board = models.BooleanField()
	manpon = models.BooleanField()
	pin = models.BooleanField()
	bench_notes = models.CharField(max_length=60, blank=True)
	bands = models.CharField(max_length=60, blank=True)
	chains = models.CharField(max_length=60, blank=True)
	movement_weight = models.IntegerField(default=0)
	movement_reps = models.IntegerField(default=0)


class UpperAccessoryMovement(models.Model):
	user = models.ForeignKey('auth.User')
	created_at = models.DateTimeField(default=timezone.now)
	top_set = models.CharField(max_length=60,blank=True)
	close_grippness = models.CharField(max_length=60,blank=True)
	tate_press = models.CharField(max_length=60,blank=True)
	dips = models.CharField(max_length=60,blank=True)
	rev_db_fly = models.CharField(max_length=60,blank=True)
	windmills = models.CharField(max_length=60,blank=True)
	bamboo_bar = models.CharField(max_length=60,blank=True)
	lat_pulldowns = models.CharField(max_length=60,blank=True)
	lat_pullovers = models.CharField(max_length=60,blank=True)
	pec_dec = models.CharField(max_length=60,blank=True)
	reverse_pec_dec = models.CharField(max_length=60,blank=True)
	t_bar_rows = models.CharField(max_length=60,blank=True)
	chest_supported_rows = models.CharField(max_length=60,blank=True)
	low_rows = models.CharField(max_length=60,blank=True)
	pullups = models.CharField(max_length=60,blank=True)
	inverted_row = models.CharField(max_length=60,blank=True)
	face_pulls = models.CharField(max_length=60,blank=True)
	db_rows = models.CharField(max_length=60,blank=True)
	db_press = models.CharField(max_length=60,blank=True)
	pullaparts = models.CharField(max_length=60,blank=True)
	tri_extensions = models.CharField(max_length=60,blank=True)
	skull_crushers = models.CharField(max_length=60,blank=True)
	jam_press = models.CharField(max_length=60,blank=True)
	olt_press = models.CharField(max_length=60,blank=True)
	db_rollbacks = models.CharField(max_length=60,blank=True)
	dead_press = models.CharField(max_length=60,blank=True)
	ab_movement = models.CharField(max_length=60,blank=True)
	notes = models.CharField(max_length=300, blank=True)





class LowerAccessoryMovement(models.Model):
	user = models.ForeignKey('auth.User')
	created_at = models.DateTimeField(default=timezone.now)
	top_set = models.CharField(max_length=60,blank=True)
	chair_dl = models.CharField(max_length=60,blank=True)
	ghr = models.CharField(max_length=60,blank=True)
	lunge = models.CharField(max_length=60,blank=True)
	dimel_dl = models.CharField(max_length=60,blank=True)
	reverse_hyper = models.CharField(max_length=60,blank=True)
	hip_bridge = models.CharField(max_length=60,blank=True)
	good_morning = models.CharField(max_length=60,blank=True)
	step_up = models.CharField(max_length=60,blank=True)
	belt_squat = models.CharField(max_length=60,blank=True)
	hack_squat = models.CharField(max_length=60,blank=True)
	leg_press = models.CharField(max_length=60,blank=True)
	leg_curl = models.CharField(max_length=60,blank=True)
	stiff_leg_dl = models.CharField(max_length=60,blank=True)
	inverse_curl = models.CharField(max_length=60,blank=True)
	front_squat = models.CharField(max_length=60,blank=True)
	back_extension = models.CharField(max_length=60,blank=True)
	ab_movement = models.CharField(max_length=60,blank=True)
	notes = models.CharField(max_length=300, blank=True)
