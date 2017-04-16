from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from .models import SquatMovement, DeadliftMovement, BenchMovement, LowerAccessoryMovement, UpperAccessoryMovement

def index(request):
    latest_squat_list = SquatMovement.objects.order_by('-created_at')[:5]
    latest_deadlift_list = DeadliftMovement.objects.order_by('-created_at')[:5]
    latest_bench_list = BenchMovement.objects.order_by('-created_at')[:5]
    latest_loweraccessory_list = LowerAccessoryMovement.objects.order_by('-created_at')[:5]
    latest_upperaccessory_list = UpperAccessoryMovement.objects.order_by('-created_at')[:5]
    context = {
        'latest_squat_list': latest_squat_list,
        'latest_deadlift_list': latest_deadlift_list,
        'latest_bench_list': latest_bench_list,
        'latest_loweraccessory_list': latest_loweraccessory_list,
        'latest_upperaccessory_list': latest_upperaccessory_list,

    }
    return render(request, 'tracker/index.html', context)

class DetailView(generic.DetailView):
    model = SquatMovement
    template_name = 'tracker/detail.html'


def new(request):

    new_workout = SquatMovement(pub_date=timezone.now(),upper_body=request.POST['upper_body'],lower_body=request.POST['lower_body'],max_effort=request.POST['max_effort'],
        dynamic_effort=request.POST['dynamic_effort'],barbell_workout=request.POST['barbell_workout'],dumbbell_workout=request.POST['dumbbell_workout'],bar_type=request.POST['bar_type'],
        acc_resistance=request.POST['acc_resistance'], box_free=request.POST['box_free'])
    new_workout.save()
    return HttpResponseRedirect('/tracker/  ')
