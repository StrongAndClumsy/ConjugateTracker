from django import forms
from .models import SquatMovement, DeadliftMovement, BenchMovement, LowerAccessoryMovement, UpperAccessoryMovement
from django.utils import timezone


EFFORT_CHOICES = (('Dynamic', 'Dynamic Effort'), ('Max', 'Max Effort'))
BOXFREE_CHOICES = (('Free', 'Free'), ('Box', 'Box'))
SUMO_CHOICES = (('Sumo', 'Sumo'), ('Conventional', 'Conventional'))
BAR_OPTIONS = (('Straight', 'Straight'), ('Giant Cambered', 'Giant Cambered'), ('Buffalo', 'Buffalo'), ('Bow', 'Bow'), ('Safety Squat Bar', 'Safety Squat Bar'))
BENCH_BAR_OPTIONS = (('Straight', 'Straight'), ('Cambered', 'Cambered'), ('Bow', 'Bow'), ('Football Bar', 'Football Bar'))
BAND_TYPE = (('None', 'None'), ('Micro Mini', 'Micro Mini'), ('Mini', 'Mini'), ('Monster Mini', 'Monster Mini '), ('Light', 'Light'), ('Average', 'Average'), ('Heavy', 'Heavy'))
BOARD = (('0', 'None'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))

class SquatForm(forms.ModelForm):
	class Meta:
		model = SquatMovement
		fields = ['created_at','box_free','effort_type','bar_type','bands_type', 'reverse', 'chain_weight',
		'movement_weight', 'movement_sets', 'movement_reps','squat_notes', 'media_url']
	created_at = forms.DateTimeField(initial=timezone.now)
	effort_type = forms.ChoiceField(label="Day", widget=forms.RadioSelect(), choices=EFFORT_CHOICES)
	box_free = forms.ChoiceField(label="Squat Type", widget=forms.RadioSelect, choices=BOXFREE_CHOICES)
	bar_type = forms.ChoiceField(label="Bar Type", widget=forms.Select, choices=BAR_OPTIONS, required=True)
	bands_type = forms.ChoiceField(label="Band Type", widget=forms.Select, choices=BAND_TYPE, required=False)
	reverse = forms.BooleanField(label="Reverse Band",required=False)
	chain_weight = forms.IntegerField(required=False, initial=0)
	movement_weight = forms.IntegerField(label="Bar Weight", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 150'}))
	movement_sets = forms.IntegerField(label="Sets", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	movement_reps = forms.IntegerField(label="Reps", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	squat_notes = forms.CharField(max_length=300,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Squat Notes Here'}),required=False)
	media_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Media URL Here'}),required=False)

class SquatSearchForm(forms.ModelForm):
	class Meta:
		model = SquatMovement
		fields = ['box_free','effort_type','bar_type','bands_type','reverse', 'chain_weight',
		'movement_weight', 'movement_sets', 'movement_reps','squat_notes', 'media_url']
	effort_type = forms.ChoiceField(label="Day", widget=forms.RadioSelect(), choices=EFFORT_CHOICES)
	box_free = forms.ChoiceField(label="Squat Type", widget=forms.RadioSelect, choices=BOXFREE_CHOICES)
	bar_type = forms.CharField(max_length=60)
	bands_type = forms.CharField(label="Band Type", required=False, max_length=60)
	reverse = forms.BooleanField(label="Reverse Band",required=False)
	chain_weight = forms.IntegerField(required=False, initial=0)
	movement_weight = forms.IntegerField(label="Bar Weight", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 150'}))
	movement_sets = forms.IntegerField(label="Sets", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	movement_reps = forms.IntegerField(label="Reps", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	squat_notes = forms.CharField(max_length=300,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Squat Notes Here'}),required=False)
	media_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Media URL Here'}),required=False)

class DeadliftForm(forms.ModelForm):
	class Meta:
		model = DeadliftMovement
		fields = ['created_at','effort_type','sumo_conventional','deficit','block','standard','pin', 'reverse','chain_weight', 'bands_type',
		'movement_weight','movement_sets','movement_reps','deadlift_notes', 'media_url']
	created_at = forms.DateTimeField(initial=timezone.now)
	effort_type = forms.ChoiceField(label="Day", widget=forms.RadioSelect(), choices=EFFORT_CHOICES)
	sumo_conventional = forms.ChoiceField(label="Deadlift Style",widget=forms.RadioSelect, choices=SUMO_CHOICES)
	deficit = forms.BooleanField(required=False)
	block = forms.BooleanField(required=False)
	standard = forms.BooleanField(required=False)
	pin = forms.BooleanField(required=False)
	reverse = forms.BooleanField(label="Reverse Band",required=False)
	bands_type = forms.ChoiceField(label="Band Type", widget=forms.Select, choices=BAND_TYPE, required=False)
	chain_weight = forms.IntegerField(required=False, initial=0)
	movement_weight = forms.IntegerField(label="Bar Weight", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 120'}))
	movement_sets = forms.IntegerField(label="Sets", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	movement_reps = forms.IntegerField(label="Reps", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	deadlift_notes = forms.CharField(required=False,max_length=300,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Deadlift Notes Here'}))
	media_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Media URL Here'}),required=False)

class DeadliftSearchForm(forms.ModelForm):
	class Meta:
		model = DeadliftMovement
		fields = ['effort_type','sumo_conventional','deficit','block','standard','pin','chain_weight', 'bands_type',
		'reverse','movement_weight', 'movement_sets','movement_reps','deadlift_notes', 'media_url']
	effort_type = forms.ChoiceField(label="Day", widget=forms.RadioSelect(), choices=EFFORT_CHOICES)
	sumo_conventional = forms.ChoiceField(label="Deadlift Style",widget=forms.RadioSelect, choices=SUMO_CHOICES)
	deficit = forms.BooleanField(required=False)
	block = forms.BooleanField(required=False)
	standard = forms.BooleanField(required=False)
	pin = forms.BooleanField(required=False)
	reverse = forms.BooleanField(label="Reverse Band",required=False)
	bands_type = forms.ChoiceField(label="Band Type", widget=forms.Select, choices=BAND_TYPE, required=False)
	chain_weight = forms.IntegerField(required=False, initial=0)
	movement_weight = forms.IntegerField(label="Bar Weight", required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 120'}))
	movement_sets = forms.IntegerField(label="Sets", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	movement_reps = forms.IntegerField(label="Reps", required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	deadlift_notes = forms.CharField(required=False,max_length=300,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Deadlift Notes Here'}))
	media_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Media URL Here'}),required=False)

class BenchForm(forms.ModelForm):
	class Meta:
		model = BenchMovement
		fields = ['created_at','effort_type','bar_type','floor','reverse','board','manpon',
		'pin','bands_type','chain_weight','movement_weight', 'movement_sets','movement_reps','bench_notes', 'media_url']
	created_at = forms.DateTimeField(initial=timezone.now)
	effort_type = forms.ChoiceField(label="Day", widget=forms.RadioSelect(), choices=EFFORT_CHOICES)
	bar_type = forms.ChoiceField(label="Bar Type", widget=forms.Select, choices=BENCH_BAR_OPTIONS, required=True)
	floor = forms.BooleanField(label="Floor Press",required=False)
	reverse = forms.BooleanField(label="Reverse Band",required=False)
	board = forms.ChoiceField(label="Boards", widget=forms.Select, choices=BOARD, required=False)
	manpon = forms.BooleanField(required=False)
	pin = forms.BooleanField(required=False)
	bands_type = forms.ChoiceField(label="Band Type", widget=forms.Select, choices=BAND_TYPE, required=False)
	chain_weight = forms.IntegerField(required=False, initial=0)
	movement_weight = forms.IntegerField(label="Bar Weight",required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 150'}))
	movement_sets = forms.IntegerField(label="Sets", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	movement_reps = forms.IntegerField(label="Reps",required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	bench_notes = forms.CharField(required=False,max_length=300,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Bench Notes Here'}))
	media_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Media URL Here'}),required=False)

class BenchSearchForm(forms.ModelForm):
	class Meta:
		model = BenchMovement
		fields = ['effort_type','bar_type','floor','reverse','board','manpon',
		'pin','bands_type','chain_weight','movement_weight', 'movement_sets','movement_reps','bench_notes', 'media_url']
	effort_type = forms.ChoiceField(label="Day", widget=forms.RadioSelect(), choices=EFFORT_CHOICES)
	bar_type = forms.ChoiceField(label="Bar Type", widget=forms.Select, choices=BENCH_BAR_OPTIONS, required=False)
	floor = forms.BooleanField(label="Floor Press",required=False)
	reverse = forms.BooleanField(label="Reverse Band",required=False)
	board = forms.ChoiceField(label="Boards", widget=forms.Select, choices=BOARD, required=False)
	manpon = forms.BooleanField(required=False)
	pin = forms.BooleanField(required=False)
	bands_type = forms.ChoiceField(label="Band Type", widget=forms.Select, choices=BAND_TYPE, required=False)
	chain_weight = forms.IntegerField(required=False, initial=0)
	movement_weight = forms.IntegerField(label="Bar Weight",required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 150'}))
	movement_sets = forms.IntegerField(label="Sets", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	movement_reps = forms.IntegerField(label="Reps",required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1'}))
	bench_notes = forms.CharField(required=False,max_length=300,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Bench Notes Here'}))
	media_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Media URL Here'}),required=False)


class UpperForm(forms.ModelForm):
	class Meta:
		model = UpperAccessoryMovement
		fields = ['created_at','top_set','close_grippness','tate_press','dips','rev_db_fly',
		'windmills','bamboo_bar','lat_pulldowns','lat_pullovers','pec_dec',
		'reverse_pec_dec','t_bar_rows','chest_supported_rows','low_rows',
		'pullups','inverted_row','face_pulls','db_rows','db_press','pullaparts',
		'tri_extensions','skull_crushers','jam_press','olt_press','db_rollbacks',
		'dead_press','ab_movement', 'other', 'notes', 'media_url']
	created_at = forms.DateTimeField(initial=timezone.now)
	top_set = forms.CharField(required=False,max_length=60)
	close_grippness = forms.CharField(label="Close Grip",required=False,max_length=60)
	tate_press = forms.CharField(required=False,max_length=60)
	dips = forms.CharField(required=False,max_length=60)
	rev_db_fly = forms.CharField(label="Rev DB Fly",required=False,max_length=60)
	windmills = forms.CharField(required=False,max_length=60)
	bamboo_bar = forms.CharField(required=False,max_length=60)
	lat_pulldowns = forms.CharField(required=False,max_length=60)
	lat_pullovers = forms.CharField(required=False,max_length=60)
	pec_dec = forms.CharField(required=False,max_length=60)
	reverse_pec_dec = forms.CharField(required=False,max_length=60)
	t_bar_rows = forms.CharField(required=False,max_length=60)
	chest_supported_rows = forms.CharField(required=False,max_length=60)
	low_rows = forms.CharField(required=False,max_length=60)
	pullups = forms.CharField(required=False,max_length=60)
	inverted_row = forms.CharField(required=False,max_length=60)
	face_pulls = forms.CharField(required=False,max_length=60)
	db_rows = forms.CharField(label="DB Rows",required=False,max_length=60)
	db_press = forms.CharField(label="DB Press",required=False,max_length=60)
	pullaparts = forms.CharField(required=False,max_length=60)
	tri_extensions = forms.CharField(required=False,max_length=60)
	skull_crushers = forms.CharField(required=False,max_length=60)
	jam_press = forms.CharField(label="JM Press",required=False,max_length=60)
	olt_press = forms.CharField(label="Overhead Press",required=False,max_length=60)
	db_rollbacks = forms.CharField(label="DB Rollbacks",required=False,max_length=60)
	dead_press = forms.CharField(required=False,max_length=60)
	ab_movement = forms.CharField(required=False,max_length=60)
	other = forms.CharField(required=False,max_length=60)
	notes = forms.CharField(required=False,max_length=300,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Upper Accessory Notes Here'}))
	media_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Media URL Here'}),required=False)


class LowerForm(forms.ModelForm):
	class Meta:
		model = LowerAccessoryMovement
		fields = ['created_at','top_set','chair_dl','ghr','lunge','dimel_dl',
		'reverse_hyper','hip_bridge','good_morning', 'step_up',
		'belt_squat','hack_squat','leg_press','leg_curl','stiff_leg_dl',
		'inverse_curl','front_squat','back_extension','ab_movement','notes', 'other', 'media_url']
	created_at = forms.DateTimeField(initial=timezone.now)
	top_set = forms.CharField(required=False,max_length=60)
	chair_dl = forms.CharField(label="Chair Deadlift",required=False,max_length=60)
	ghr = forms.CharField(label="GHR",required=False,max_length=60)
	lunge = forms.CharField(required=False,max_length=60)
	dimel_dl = forms.CharField(label="Dimel DL",required=False,max_length=60)
	reverse_hyper = forms.CharField(required=False,max_length=60)
	hip_bridge = forms.CharField(required=False,max_length=60)
	good_morning = forms.CharField(required=False,max_length=60)
	step_up = forms.CharField(required=False,max_length=60)
	belt_squat = forms.CharField(required=False,max_length=60)
	hack_squat = forms.CharField(required=False,max_length=60)
	leg_press = forms.CharField(required=False,max_length=60)
	leg_curl = forms.CharField(required=False,max_length=60)
	stiff_leg_dl = forms.CharField(label="Stiff Leg DL",required=False,max_length=60)
	inverse_curl = forms.CharField(required=False,max_length=60)
	front_squat = forms.CharField(required=False,max_length=60)
	back_extension = forms.CharField(required=False,max_length=60)
	ab_movement = forms.CharField(required=False,max_length=60)
	other = forms.CharField(required=False,max_length=60)
	notes = forms.CharField(required=False,max_length=300,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Lower Accessory Notes Here'}))
	media_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Media URL Here'}),required=False)
