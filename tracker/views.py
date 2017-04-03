from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from .models import Workout

def index(request):
    latest_workout_list = Workout.objects.order_by('-pub_date')[:5]
    context = {
        'latest_workout_list': latest_workout_list,
    }
    return render(request, 'tracker/index.html', context)

class DetailView(generic.DetailView):
    model = Workout
    template_name = 'tracker/detail.html'


def new(request):

    new_workout = Workout(pub_date=timezone.now(),upper_body=request.POST['upper_body'],lower_body=request.POST['lower_body'],max_effort=request.POST['max_effort'],
        dynamic_effort=request.POST['dynamic_effort'],barbell_workout=request.POST['barbell_workout'],dumbbell_workout=request.POST['dumbbell_workout'],bar_type=request.POST['bar_type'],
        acc_resistance=request.POST['acc_resistance'], box_free=request.POST['box_free'])
    new_workout.save()
    return HttpResponseRedirect('/tracker/')
