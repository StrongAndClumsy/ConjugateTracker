from django.db import models

# Create your models here.
class Workout(models.Model):
	pub_date = models.DateTimeField('date published')
	upper_body = models.NullBooleanField()
	lower_body = models.NullBooleanField()
	dynamic_effort = models.NullBooleanField()
	max_effort = models.NullBooleanField()
	barbell_workout = models.NullBooleanField()
	dumbbell_workout = models.NullBooleanField()
	bar_type = models.CharField(max_length=60)
	acc_resistance = models.CharField(max_length=60)
	box_free = models.CharField(max_length=60)
