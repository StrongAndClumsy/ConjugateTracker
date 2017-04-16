from django.conf.urls import url

from . import views
app_name = "tracker"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^workout/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^workout/new$', views.new, name='new'),
]
