from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.db.models import Q
import os
from .models import SquatMovement, DeadliftMovement, BenchMovement, LowerAccessoryMovement, UpperAccessoryMovement
from .forms import SquatForm, SquatSearchForm, DeadliftForm, DeadliftSearchForm, BenchForm, BenchSearchForm, LowerForm, UpperForm
import pygal
from pygal.style import NeonStyle
import random

IMAGE_PATH = os.getenv('BASEPATH', default="")

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
    return render(request, 'registration_form.html', {'form': form})

def index(request):
    if not request.user.is_authenticated:
        #return redirect('%s?next=%s' % ('/login/', request.path))
        return render(request, 'tracker/landing_page.html')
    else:
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
        return render(request, 'tracker/home_page.html', context)

def new_squat(request):
    if request.method == 'POST':
        form = SquatForm(request.POST)
        if form.is_valid():
            new_squat_data = SquatMovement(
                user = request.user,
                created_at = form.cleaned_data['created_at'],
                effort_type = form.cleaned_data['effort_type'],
                box_free = form.cleaned_data['box_free'],
                bar_type = form.cleaned_data['bar_type'],
                bands_type = form.cleaned_data['bands_type'],
                reverse = form.cleaned_data['reverse'],
                chain_weight = form.cleaned_data['chain_weight'],
                movement_weight = form.cleaned_data['movement_weight'],
                movement_sets = form.cleaned_data['movement_sets'],
                movement_reps = form.cleaned_data['movement_reps'],
                squat_notes = form.cleaned_data['squat_notes'],
                media_url = form.cleaned_data['media_url'])
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
                created_at = form.cleaned_data['created_at'],
                effort_type = form.cleaned_data['effort_type'],
                sumo_conventional=form.cleaned_data['sumo_conventional'],
                deficit=form.cleaned_data['deficit'],
                block=form.cleaned_data['block'],
                standard=form.cleaned_data['standard'],
                pin=form.cleaned_data['pin'],
                reverse=form.cleaned_data['reverse'],
                bands_type=form.cleaned_data['bands_type'],
                chain_weight=form.cleaned_data['chain_weight'],
                movement_weight=form.cleaned_data['movement_weight'],
                movement_sets=form.cleaned_data['movement_sets'],
                movement_reps=form.cleaned_data['movement_reps'],
                deadlift_notes=form.cleaned_data['deadlift_notes'],
                media_url=form.cleaned_data['media_url']
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
                created_at=form.cleaned_data['created_at'],
                effort_type=form.cleaned_data['effort_type'],
                bar_type=form.cleaned_data['bar_type'],
                floor=form.cleaned_data['floor'],
                reverse=form.cleaned_data['reverse'],
                board=form.cleaned_data['board'],
                manpon=form.cleaned_data['manpon'],
                pin=form.cleaned_data['pin'],
                bench_notes=form.cleaned_data['bench_notes'],
                bands_type=form.cleaned_data['bands_type'],
                chain_weight=form.cleaned_data['chain_weight'],
                movement_weight=form.cleaned_data['movement_weight'],
                movement_sets=form.cleaned_data['movement_sets'],
                movement_reps=form.cleaned_data['movement_reps'],
                media_url=form.cleaned_data['media_url']
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
                created_at=form.cleaned_data['created_at'],
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
                ab_movement=form.cleaned_data['ab_movement'],
                other=form.cleaned_data['other'],
                notes=form.cleaned_data['notes'],
                media_url=form.cleaned_data['media_url']
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
                created_at=form.cleaned_data['created_at'],
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
                ab_movement=form.cleaned_data['ab_movement'],
                other=form.cleaned_data['other'],
                notes=form.cleaned_data['notes'],
                media_url=form.cleaned_data['media_url']
                )
            new_upper_data.save()
            return HttpResponseRedirect('/')
    else:
        form = UpperForm()
    return render(request, 'new_upper.html', {'form': form})


def squat_edit(request, pk):
    squat = get_object_or_404(SquatMovement, pk=pk)
    if request.method == "POST":
        form = SquatForm(request.POST, instance=squat)
        if form.is_valid():
            squat = form.save(commit=False)
            squat.save()
            return render(request, 'tracker/squatmovement_detail.html', {'object': squat})
    else:
        form = SquatForm(instance=squat)
    return render(request, 'edit_squat.html', {'form': form, 'pk': pk})

def bench_edit(request, pk):
    bench = get_object_or_404(BenchMovement, pk=pk)
    if request.method == "POST":
        form = BenchForm(request.POST, instance=bench)
        if form.is_valid():
            bench = form.save(commit=False)
            bench.save()
            return render(request, 'tracker/benchmovement_detail.html', {'object': bench})
    else:
        form = BenchForm(instance=bench)
    return render(request, 'edit_bench.html', {'form': form, 'pk': pk})

def deadlift_edit(request, pk):
    deadlift = get_object_or_404(DeadliftMovement, pk=pk)
    if request.method == "POST":
        form = DeadliftForm(request.POST, instance=deadlift)
        if form.is_valid():
            deadlift = form.save(commit=False)
            deadlift.save()
            return render(request, 'tracker/deadliftmovement_detail.html', {'object': deadlift})
    else:
        form = DeadliftForm(instance=deadlift)
    return render(request, 'edit_deadlift.html', {'form': form, 'pk': pk})

def upper_edit(request, pk):
    upper = get_object_or_404(UpperAccessoryMovement, pk=pk)
    if request.method == "POST":
        form = UpperForm(request.POST, instance=upper)
        if form.is_valid():
            upper = form.save(commit=False)
            upper.save()
            return render(request, 'tracker/upperaccessorymovement_detail.html', {'object': upper})
    else:
        form = UpperForm(instance=upper)
    return render(request, 'edit_upper.html', {'form': form, 'pk': pk})

def lower_edit(request, pk):
    lower = get_object_or_404(LowerAccessoryMovement, pk=pk)
    if request.method == "POST":
        form = LowerForm(request.POST, instance=lower)
        if form.is_valid():
            lower = form.save(commit=False)
            lower.save()
            return render(request, 'tracker/loweraccessorymovement_detail.html', {'object': lower})
    else:
        form = LowerForm(instance=lower)
    return render(request, 'edit_lower.html', {'form': form, 'pk': pk})

def squat_search(request):
    if request.method == "GET":
        search_dict = request.GET.dict()
        filter_dict = {}
        for key, value in search_dict.items():
            if value != ''and value != "None":
                filter_dict[key] = value
        if len(filter_dict) > 0:
            print(filter_dict)
            filtered_movements = SquatMovement.objects.filter(user_id=request.user.id).filter(**filter_dict)
            print(filtered_movements)
            form = SquatSearchForm()
            return render(request, 'tracker/squatmovement_search.html', {'form': form, 'objects': filtered_movements})
        else:
            form = SquatSearchForm()
            return render(request, 'tracker/squatmovement_search.html', {'form': form })
    return render(request, 'Request type not allowed.' )

def bench_search(request):
    if request.method == "GET":
        search_dict = request.GET.dict()
        filter_dict = {}
        for key, value in search_dict.items():
            if value != ''and value != "None":
                filter_dict[key] = value
        if len(filter_dict) > 0:
            print(filter_dict)
            filtered_movements = BenchMovement.objects.filter(user_id=request.user.id).filter(**filter_dict)
            form = BenchSearchForm()
            return render(request, 'tracker/benchmovement_search.html', {'form': form, 'objects': filtered_movements})
        else:
            form = BenchSearchForm()
            return render(request, 'tracker/benchmovement_search.html', {'form': form })
    return render(request, 'Request type not allowed.' )

def deadlift_search(request):
    if request.method == "GET":
        search_dict = request.GET.dict()
        filter_dict = {}
        for key, value in search_dict.items():
            if value != '' and value != "None":
                filter_dict[key] = value
        if len(filter_dict) > 0:
            filtered_movements = DeadliftMovement.objects.filter(user_id=request.user.id).filter(**filter_dict)
            form = DeadliftSearchForm()
            return render(request, 'tracker/deadliftmovement_search.html', {'form': form, 'objects': filtered_movements})
        else:
            form = DeadliftSearchForm()
            return render(request, 'tracker/deadliftmovement_search.html', {'form': form })
    return render(request, 'Request type not allowed.' )

def upper_search(request):
    if request.method == "GET":
        search_dict = request.GET.dict()
        filter_dict = {}
        for key, value in search_dict.items():
            if value != ''and value != "None" and key != "created_at":
                filter_dict[key] = ''
        if len(filter_dict) > 0:
            filtered_movements = UpperAccessoryMovement.objects.filter(user_id=request.user.id).filter(~Q(**filter_dict))
            print(filtered_movements)
            form = UpperForm()
            return render(request, 'tracker/uppermovement_search.html', {'form': form, 'objects': filtered_movements})
        else:
            form = UpperForm()
            return render(request, 'tracker/uppermovement_search.html', {'form': form })
    return render(request, 'Request type not allowed.')

def lower_search(request):
    if request.method == "GET":
        search_dict = request.GET.dict()
        filter_dict = {}
        for key, value in search_dict.items():
            if value != ''and value != "None" and key != "created_at":
                filter_dict[key] = ''
        if len(filter_dict) > 0:
            filtered_movements = LowerAccessoryMovement.objects.filter(user_id=request.user.id).filter(~Q(**filter_dict))
            form = LowerForm()
            return render(request, 'tracker/lowermovement_search.html', {'form': form, 'objects': filtered_movements})
        else:
            form = LowerForm()
            return render(request, 'tracker/lowermovement_search.html', {'form': form })
    return render(request, 'Request type not allowed.' )


def analysis(request):
    if request.method == "GET":
        version = random.randint(0, 1000)
        search_dict = request.GET.dict()
        filter_dict = {}
        for key, value in search_dict.items():
            #Bench
            if key == "movement1" and value == "bench1":
                for key, value in search_dict.items():
                    if value != '' and value != "None" and key != "movement1":
                        filter_dict[key] = value
                if len(filter_dict) > 0:
                    print(filter_dict)
                    filtered_movements = BenchMovement.objects.filter(user_id=request.user.id).filter(**filter_dict)
                    max_weight = []
                    for workout in filtered_movements:
                        max_weight.append(workout.movement_weight)
                    line_chart = pygal.Line(style=NeonStyle)
                    line_chart.title = 'Lift Progression'
                    line_chart.x_labels = map(str, range(1, len(max_weight)))
                    line_chart.add('Bench', max_weight)
                    line_chart.render_to_file(IMAGE_PATH + 'tracker/static/tmp/chart.svg')

            # Deadlift
            if key == "movement1" and value == "deadlift1":
                for key, value in search_dict.items():
                    if value != '' and value != "None" and key != "movement1":
                        filter_dict[key] = value
                if len(filter_dict) > 0:
                    print(filter_dict)
                    filtered_movements = DeadliftMovement.objects.filter(user_id=request.user.id).filter(**filter_dict)
                    max_weight = []
                    for workout in filtered_movements:
                        max_weight.append(workout.movement_weight)
                    line_chart = pygal.Line(style=NeonStyle)
                    line_chart.title = 'Lift Progression'
                    line_chart.x_labels = map(str, range(1, len(max_weight)))
                    line_chart.add('Deadlift', max_weight)
                    line_chart.render_to_file(IMAGE_PATH + 'tracker/static/tmp/chart.svg')

            # Squat
            if key == "movement1" and value == "squat1":
                for key, value in search_dict.items():
                    if value != '' and value != "None" and key != "movement1":
                        filter_dict[key] = value
                if len(filter_dict) > 0:
                    print(filter_dict)
                    filtered_movements = SquatMovement.objects.filter(user_id=request.user.id).filter(**filter_dict)
                    max_weight = []
                    for workout in filtered_movements:
                        max_weight.append(workout.movement_weight)
                    line_chart = pygal.Line(style=NeonStyle)
                    line_chart.title = 'Lift Progression'
                    line_chart.x_labels = map(str, range(1, len(max_weight)))
                    line_chart.add('Squat', max_weight)
                    line_chart.render_to_file(IMAGE_PATH + 'tracker/static/tmp/chart.svg')

            # Upper
            if key == "movement1" and value == "upper1":
                for key, value in search_dict.items():
                    if value != '' and value != "None" and key != "movement1":
                        filter_dict[key] = value
                if len(filter_dict) > 0:
                    print(filter_dict)
                    filtered_movements = SquatMovement.objects.filter(user_id=request.user.id).filter(**filter_dict)
                    max_weight = []
                    for workout in filtered_movements:
                        max_weight.append(workout.movement_weight)
                    line_chart = pygal.Line(style=NeonStyle)
                    line_chart.title = 'Lift Progression'
                    line_chart.x_labels = map(str, range(1, len(max_weight)))
                    line_chart.add('Squat', max_weight)
                    line_chart.render_to_file(IMAGE_PATH + 'tracker/static/tmp/chart.svg')

    upperform = UpperForm()
    lowerform = LowerForm()
    return render(request, 'tracker/analysis.html', {'upper_form': upperform, 'lower_form': lowerform, 'version': version})
