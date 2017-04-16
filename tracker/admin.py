from django.contrib import admin

# Register your models here.
from .models import SquatMovement, DeadliftMovement, BenchMovement, UpperAccessoryMovement, LowerAccessoryMovement

admin.site.register(SquatMovement)
admin.site.register(DeadliftMovement)
admin.site.register(BenchMovement)
admin.site.register(UpperAccessoryMovement)
admin.site.register(LowerAccessoryMovement)
