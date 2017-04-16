from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from .models import SquatMovement, DeadliftMovement, BenchMovement, LowerAccessoryMovement, UpperAccessoryMovement
from .forms import SquatForm, DeadliftForm, BenchForm, LowerForm, UpperForm

class SquatDetailView(DetailView):
    model = SquatMovement
    def get_context_data(self, **kwargs):
        context = super(SquatDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def index(request):
    latest_squat_list = SquatMovement.objects.order_by('-created_at')[:5]
    latest_deadlift_list = DeadliftMovement.objects.order_by('-created_at')[:5]
    latest_bench_list = BenchMovement.objects.order_by('-created_at')[:5]
    latest_loweraccessory_list = LowerAccessoryMovement.objects.order_by('-created_at')[:5]
    latest_upperaccessory_list = UpperAccessoryMovement.objects.order_by('-created_at')[:5]
    context = {
        'user_name': request.user.username,
        'latest_squat_list': latest_squat_list,
        'latest_deadlift_list': latest_deadlift_list,
        'latest_bench_list': latest_bench_list,
        'latest_loweraccessory_list': latest_loweraccessory_list,
        'latest_upperaccessory_list': latest_upperaccessory_list,
    }
    return render(request, 'tracker/index.html', context)

def new_squat(request):
    if request.method == 'POST':
        form = SquatForm(request.POST)
        if form.is_valid():
            effort = form.cleaned_data['effort_type']
            box_free = form.cleaned_data['box_free']
            bar_type = form.cleaned_data['bar_type']
            bands_type = form.cleaned_data['bands_type']
            chain_weight = form.cleaned_data['chain_weight']
            movement_weight = form.cleaned_data['movement_weight']
            movement_reps = form.cleaned_data['movement_reps']
            new_squat_data = SquatMovement( user = request.user, effort_type = effort, box_free = box_free, bar_type = bar_type, bands_type = bands_type,
                chain_weight = chain_weight, movement_weight = movement_weight,movement_reps = movement_reps)
            new_squat_data.save()
            return HttpResponseRedirect('/tracker/')
    else:
        form = SquatForm()
    return render(request, 'new_squat.html', {'form': form})

def new_deadlift(request):
    if request.method == 'POST':
        form = DeadliftForm(request.POST)
        if form.is_valid():
            new_deadlift_data = DeadliftMovement(
                user=request.user,
                sumo_conventional=form.cleaned_data['sumo_conventional'],
                deficit=form.cleaned_data['deficit'],
                block=form.cleaned_data['block'],
                standard=form.cleaned_data['standard'],
                pin=form.cleaned_data['pin'],
                reverse=form.cleaned_data['reverse'],
                movement_weight=form.cleaned_data['movement_weight'],
                movement_reps=form.cleaned_data['movement_reps'],
                deadlift_notes=form.cleaned_data['deadlift_notes']
            )
            new_deadlift_data.save()
            return HttpResponseRedirect('/tracker/')
    else:
        form = DeadliftForm()
    return render(request, 'new_deadlift.html', {'form': form})

def new_bench(request):
    if request.method == 'POST':
        form = BenchForm(request.POST)
        if form.is_valid():
            effort = form.cleaned_data['effort_type']
            box_free = form.cleaned_data['box_free']
            bar_type = form.cleaned_data['bar_type']
            bands_type = form.cleaned_data['bands_type']
            chain_weight = form.cleaned_data['chain_weight']
            movement_weight = form.cleaned_data['movement_weight']
            movement_reps = form.cleaned_data['movement_reps']
            new_bench_data = SquatMovement( user = request.user, effort_type = effort, box_free = box_free, bar_type = bar_type, bands_type = bands_type,
                chain_weight = chain_weight, movement_weight = movement_weight,movement_reps = movement_reps)
            new_bench_data.save()
            return HttpResponseRedirect('/tracker/')
    else:
        form = BenchForm()
    return render(request, 'new_bench.html', {'form': form})

def new_lower(request):
    if request.method == 'POST':
        form = LowerForm(request.POST)
        if form.is_valid():
            effort = form.cleaned_data['effort_type']
            box_free = form.cleaned_data['box_free']
            bar_type = form.cleaned_data['bar_type']
            bands_type = form.cleaned_data['bands_type']
            chain_weight = form.cleaned_data['chain_weight']
            movement_weight = form.cleaned_data['movement_weight']
            movement_reps = form.cleaned_data['movement_reps']
            new_squat_data = SquatMovement( user = request.user, effort_type = effort, box_free = box_free, bar_type = bar_type, bands_type = bands_type,
                chain_weight = chain_weight, movement_weight = movement_weight,movement_reps = movement_reps)
            new_squat_data.save()
            return HttpResponseRedirect('/tracker/')
    else:
        form = LowerForm()
    return render(request, 'new_lower.html', {'form': form})

def new_upper(request):
    if request.method == 'POST':
        form = UpperForm(request.POST)
        if form.is_valid():
            effort = form.cleaned_data['effort_type']
            box_free = form.cleaned_data['box_free']
            bar_type = form.cleaned_data['bar_type']
            bands_type = form.cleaned_data['bands_type']
            chain_weight = form.cleaned_data['chain_weight']
            movement_weight = form.cleaned_data['movement_weight']
            movement_reps = form.cleaned_data['movement_reps']
            new_squat_data = SquatMovement( user = request.user, effort_type = effort, box_free = box_free, bar_type = bar_type, bands_type = bands_type,
                chain_weight = chain_weight, movement_weight = movement_weight,movement_reps = movement_reps)
            new_squat_data.save()
            return HttpResponseRedirect('/tracker/')
    else:
        form = UpperForm()
    return render(request, 'new_upper.html', {'form': form})
