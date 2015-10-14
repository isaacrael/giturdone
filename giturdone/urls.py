from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'giturdone_quiz.views.index', name='index'),
    url(r'^quiz/', 'giturdone_quiz.views.git_quiz', name='git_quiz'),
    url(r'^account/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),

]
