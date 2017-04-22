from django.conf.urls import url
from . import views


app_name = 'chaxun'
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^captcha/$', views.captcha, name='captcha'),
    url(r'^$', views.index, name='index'),
    url(r'^query/$', views.query, name='query'),
]
