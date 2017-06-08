from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from .models import SquatMovement, DeadliftMovement, BenchMovement, LowerAccessoryMovement, UpperAccessoryMovement
from .forms import SquatForm, DeadliftForm, BenchForm, LowerForm, UpperForm

class SquatDetailView(DetailView):
    model = SquatMovement
    def get_context_data(self, **kwargs):
        context = super(SquatDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        if context['object'].user != self.request.user:
            raise Http404
        return context

class BenchDetailView(DetailView):
    model = BenchMovement
    def get_context_data(self, **kwargs):
        context = super(BenchDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        if context['object'].user != self.request.user:
            raise Http404
        return context

class DeadliftDetailView(DetailView):
    model = DeadliftMovement
    def get_context_data(self, **kwargs):
        context = super(DeadliftDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        if context['object'].user != self.request.user:
            raise Http404
        return context

class UpperDetailView(DetailView):
    model = UpperAccessoryMovement
    def get_context_data(self, **kwargs):
        context = super(UpperDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        if context['object'].user != self.request.user:
            raise Http404
        return context

class LowerDetailView(DetailView):
    model = LowerAccessoryMovement
    def get_context_data(self, **kwargs):
        context = super(LowerDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        if context['object'].user != self.request.user:
            raise Http404
        return context

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/login/', request.path))
    latest_squat_list = SquatMovement.objects.filter(user_id=request.user.id).order_by('-created_at')[:5]
    latest_deadlift_list = DeadliftMovement.objects.filter(user_id=request.user.id).order_by('-created_at')[:5]
    latest_bench_list = BenchMovement.objects.filter(user_id=request.user.id).order_by('-created_at')[:5]
    latest_loweraccessory_list = LowerAccessoryMovement.objects.filter(user_id=request.user.id).order_by('-created_at')[:5]
    latest_upperaccessory_list = UpperAccessoryMovement.objects.filter(user_id=request.user.id).order_by('-created_at')[:5]
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
            return HttpResponseRedirect('/')
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
            return HttpResponseRedirect('/')
    else:
        form = DeadliftForm()
    return render(request, 'new_deadlift.html', {'form': form})


def new_bench(request):
    if request.method == 'POST':
        form = BenchForm(request.POST)
        if form.is_valid():
            new_bench_data = BenchMovement(
                user=request.user,
                bar_type=form.cleaned_data['bar_type'],
                floor=form.cleaned_data['floor'],
                reverse=form.cleaned_data['reverse'],
                standard=form.cleaned_data['standard'],
                board=form.cleaned_data['board'],
                manpon=form.cleaned_data['manpon'],
                pin=form.cleaned_data['pin'],
                bench_notes=form.cleaned_data['bench_notes'],
                bands=form.cleaned_data['bands'],
                chains=form.cleaned_data['chains'],
                movement_weight=form.cleaned_data['movement_weight'],
                movement_reps=form.cleaned_data['movement_reps'],
                )
            new_bench_data.save()
            return HttpResponseRedirect('/')
    else:
        form = BenchForm()
    return render(request, 'new_bench.html', {'form': form})


def new_lower(request):
    if request.method == 'POST':
        form = LowerForm(request.POST)
        if form.is_valid():
            new_lower_data = LowerAccessoryMovement(
                user=request.user,
                top_set=form.cleaned_data['top_set'],
                chair_dl=form.cleaned_data['chair_dl'],
                ghr=form.cleaned_data['ghr'],
                lunge=form.cleaned_data['lunge'],
                dimel_dl=form.cleaned_data['dimel_dl'],
                reverse_hyper=form.cleaned_data['reverse_hyper'],
                hip_bridge=form.cleaned_data['hip_bridge'],
                good_morning=form.cleaned_data['good_morning'],
                step_up=form.cleaned_data['step_up'],
                belt_squat=form.cleaned_data['belt_squat'],
                hack_squat=form.cleaned_data['hack_squat'],
                leg_press=form.cleaned_data['leg_press'],
                leg_curl=form.cleaned_data['leg_curl'],
                stiff_leg_dl=form.cleaned_data['stiff_leg_dl'],
                inverse_curl=form.cleaned_data['inverse_curl'],
                front_squat=form.cleaned_data['front_squat'],
                back_extension=form.cleaned_data['back_extension'],
                ab_movement=form.cleaned_data['ab_movement']


            )
            new_lower_data.save()
            return HttpResponseRedirect('/')
    else:
        form = LowerForm()
    return render(request, 'new_lower.html', {'form': form})

def new_upper(request):
    if request.method == 'POST':
        form = UpperForm(request.POST)
        if form.is_valid():
            new_upper_data = UpperAccessoryMovement(
                user=request.user,
                top_set=form.cleaned_data['top_set'],
                close_grippness=form.cleaned_data['close_grippness'],
                tate_press=form.cleaned_data['tate_press'],
                dips=form.cleaned_data['dips'],
                rev_db_fly=form.cleaned_data['rev_db_fly'],
                windmills=form.cleaned_data['windmills'],
                bamboo_bar=form.cleaned_data['bamboo_bar'],
                lat_pulldowns=form.cleaned_data['lat_pulldowns'],
                lat_pullovers=form.cleaned_data['lat_pullovers'],
                pec_dec=form.cleaned_data['pec_dec'],
                reverse_pec_dec=form.cleaned_data['reverse_pec_dec'],
                t_bar_rows=form.cleaned_data['t_bar_rows'],
                chest_supported_rows=form.cleaned_data['chest_supported_rows'],
                low_rows=form.cleaned_data['low_rows'],
                pullups=form.cleaned_data['pullups'],
                inverted_row=form.cleaned_data['inverted_row'],
                face_pulls=form.cleaned_data['face_pulls'],
                db_rows=form.cleaned_data['db_rows'],
                db_press=form.cleaned_data['db_press'],
                pullaparts=form.cleaned_data['pullaparts'],
                tri_extensions=form.cleaned_data['tri_extensions'],
                skull_crushers=form.cleaned_data['skull_crushers'],
                jam_press=form.cleaned_data['jam_press'],
                olt_press=form.cleaned_data['olt_press'],
                db_rollbacks=form.cleaned_data['db_rollbacks'],
                dead_press=form.cleaned_data['dead_press'],
                ab_movement=form.cleaned_data['ab_movement']
                )
            new_upper_data.save()
            return HttpResponseRedirect('/')
    else:
        form = UpperForm()
    return render(request, 'new_upper.html', {'form': form})
