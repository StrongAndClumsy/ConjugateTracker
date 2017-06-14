from django.conf.urls import url
from django.http import HttpResponseRedirect, HttpResponse

from . import views
app_name = "tracker"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^squat_movement/(?P<pk>[0-9]+)/$', views.SquatDetailView.as_view(), name='squat_detail'),
    url(r'^deadlift_movement/(?P<pk>[0-9]+)/$', views.DeadliftDetailView.as_view(), name='deadlift_detail'),
    url(r'^bench_movement/(?P<pk>[0-9]+)/$', views.BenchDetailView.as_view(), name='bench_detail'),
    url(r'^lower_movement/(?P<pk>[0-9]+)/$', views.LowerDetailView.as_view(), name='lower_detail'),
    url(r'^upper_movement/(?P<pk>[0-9]+)/$', views.UpperDetailView.as_view(), name='upper_detail'),
    url(r'^squat_movement/new$', views.new_squat, name='squat_new'),
    url(r'^deadlift_movement/new$', views.new_deadlift, name='deadlift_new'),
    url(r'^bench_movement/new$', views.new_bench, name='bench_new'),
    url(r'^lower_movement/new$', views.new_lower, name='lower_new'),
    url(r'^upper_movement/new$', views.new_upper, name='upper_new'),
    url(r'^squat_movement/(?P<pk>\d+)/edit/$', views.squat_edit, name='squat_edit'),
    url(r'^bench_movement/(?P<pk>\d+)/edit/$', views.bench_edit, name='bench_edit'),
    url(r'^deadlift_movement/(?P<pk>\d+)/edit/$', views.deadlift_edit, name='deadlift_edit'),
    url(r'^upper_movement/(?P<pk>\d+)/edit/$', views.upper_edit, name='upper_edit'),
    url(r'^lower_movement/(?P<pk>\d+)/edit/$', views.lower_edit, name='lower_edit'),
]
