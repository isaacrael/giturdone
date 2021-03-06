from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # ex: /quiz/
    url(r'^quiz_selection/', views.quiz_selection, name='quiz_selection'),
#   url(r'^$', views.git_quiz, name='index'),
    url(r'^quiz/$', views.quiz, name='index'),
    url(r'^resources/', views.git_resources, name='resources'),
    # ex: /quiz/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /quiz/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^reset_scores/', views.reset_scores, name='reset_scores'),
    url(r'^short_answer_quiz_categories/', 'giturdone_quiz.views.short_answer_quiz_categories', name='short_answer_quiz_categories'),
    url(r'^feynman_technique_quiz/$', views.feynman_technique_quiz, name='feynman_technique_quiz'),
    url(r'^feynman_technique_quiz/(?P<question_id>[0-9]+)/$', 'giturdone_quiz.views.ftq_detail', name='ftq_detail'),
    url(r'^feynman_technique_quiz/(?P<question_id>[0-9]+)/results/$', 'giturdone_quiz.views.ftq_results', name='ftq_results'),
    url(r'^feynman_technique_quiz/reset_scores/$', views.ftq_reset_scores, name='ftq_reset_scores'),
    url(r'^multiple_choice_quiz/$', views.multiple_choice_quiz, name='multiple_choice_quiz'),
    url(r'^multiple_choice_quiz/(?P<question_id>[0-9]+)/$', 'giturdone_quiz.views.multiple_choice_quiz_detail', name='multiple_choice_quiz_detail'),
    url(r'^multiple_choice_quiz/(?P<question_id>[0-9]+)/vote/$', 'giturdone_quiz.views.vote', name='vote'),
    url(r'^multiple_choice_quiz/(?P<question_id>[0-9]+)/results/$', 'giturdone_quiz.views.multiple_choice_quiz_results', name='multiple_choice_quiz_results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', 'giturdone_quiz.views.vote', name='vote'),
#    url(r'^(?P<question_id>[0-9]+)/vote/results/$', 'giturdone_quiz.views.multiple_choice_quiz_results', name='multiple_choice_quiz_results'),
    # ex: /quiz/5/vote/
# Note: the answers url is not being used in the app but is left here
# as an example for future versions
#    url(r'^(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


