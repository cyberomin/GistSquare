from django.conf.urls import patterns, include, url
from article.views import UserProfileDetailView,custom_login
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', include('article.urls')),
    url(r'^$', include('article.urls')),

    (r'^accounts/', include('registration.backends.default.urls')),
    #(r'^accounts/', include('registration.backends.simple.urls')),


    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': '/templates/registration/login.html'}),
    #url(r'^accounts/profile/$', 'django.contrib.auth.views.login',{'template_name': '/templates/user_details.html'}),
    
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login',name="logout"),
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name="Profile"),
    url(r'^admin/', include(admin.site.urls)),

    #URL to redirect when a use logs in
    url('^$', 'article.views.articles', name='home'),

    #Custom URLS
    url(r'^story/(?P<article_id>\d+)/(.*)/$', 'article.views.article'),
    url(r'^story/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^create/$', 'article.views.create'),
    url(r'^story/likes/(?P<article_id>\d+)/$', 'article.views.likes'),
    url(r'^search/$', 'article.views.search_titles'),
    url(r'^subscription/$', 'article.views.email_subscribe'),
    url(r"^story/add_comment/(\d+)/$", "article.views.add_comment"),
    url(r'^likes/(?P<article_id>\d+)/$', 'article.views.likes'),
)
