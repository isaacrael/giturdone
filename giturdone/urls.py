from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


# Include namespace in the url's

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^quiz/', include('giturdone_quiz.urls', namespace="giturdone_quiz")),
    url(r'^quiz_selection/', 'giturdone_quiz.views.quiz_selection', name='quiz_selection'),
    url(r'^short_answer_quiz/', 'giturdone_quiz.views.short_answer_quiz', name='index'),
    url(r'^$', 'giturdone_quiz.views.index', name='index'),
    url(r'^results/', 'giturdone_quiz.views.results', name='results'),
# Left line below in prod version for now just in case it is needed
#    url(r'^quiz/', 'giturdone_quiz.views.git_quiz', name='git_quiz'),
    url(r'^account/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

