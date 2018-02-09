from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # ex: /quiz/
    url(r'^quiz_selection/', views.quiz_selection, name='quiz_selection'),
    url(r'^short_answer_quiz/', views.short_answer_quiz, name='index'),
    url(r'^$', views.short_answer_quiz, name='index'),
    url(r'^resources/', views.git_resources, name='resources'),
    # ex: /quiz/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /quiz/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^reset_scores/', views.reset_scores, name='reset_scores'),
    # ex: /quiz/5/vote/
# Note: the answers url is not being used in the app but is left here
# as an example for future versions
#    url(r'^(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


