from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /quiz/
    url(r'^$', views.git_quiz, name='index'),
    url(r'^resources/', views.git_resources, name='resources'),
#    url(r'^results/', views.results, name='results'),
#    url(r'^quiz/', views.index, name='index'),
    # ex: /quiz/5/
#    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /quiz/5/results/
#    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /quiz/5/vote/
#    url(r'^(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer'),
]


"""

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^/results/', views.results, name='results'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
#    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


"""