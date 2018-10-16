from django.conf.urls import url

from . import views

app_name = 'codetester'
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<submission_id>[0-9]+)/results/$', views.results, name='results'),
]