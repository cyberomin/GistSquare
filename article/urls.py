from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    (r'^$', 'article.views.articles'),
    url(r'^$', 'article.views.articles'),
    url(r'^article/$', 'article.views.articles'),
    url(r'^story/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^create/$', 'article.views.create'),
    url(r'^likes/(?P<article_id>\d+)/$', 'article.views.likes'),
    
    url(r'^subscription/$', 'article.views.email_subscribe'),
    url(r"^add_comment/(\d+)/$", "article.views.add_comment"),


)



