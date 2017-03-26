from django.db import models

# Create your models here.
class Workout(models.Model):
	pub_date = models.DateTimeField('date published')
	upper_lower = models.CharField(max_length=60)
	dynamic_max = models.CharField(max_length=60)
	bb_db = models.CharField(max_length=60)
	bar_type = models.CharField(max_length=60)
	acc_resistance = models.CharField(max_length=60)
	box_free = models.CharField(max_length=60)