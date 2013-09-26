import os

from django.shortcuts import render_to_response
from article.models import Article,Subscription,Comments,UserProfile
from forms import ArticleForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.validators import email_re


from django.views.generic import DetailView
from django.contrib.auth import get_user_model

import re
import string

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.views import login_required
#Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

HASH = []
STOP_WORDS = open(PROJECT_ROOT+"/article/common.txt").read().split("\n")
STOP_WORDS = STOP_WORDS
def trends(text):
    data_store = dict()
    #text = text.lower()
    text = text.split(" ")
    for i in text:
        if i in data_store.iterkeys() and i not in STOP_WORDS:
            val = data_store[i]
            data_store[i] = val + 1
        else:
            data_store[i] = 1
    return data_store

def sort(result):

    result = result.iteritems()
    data = []
    for k,v in result:
        data.append((v,k))
    data.sort(reverse=True)
    val = max(data)
    return val[1].title()


#@login_required
def articles(request):
    data = Article.objects.all().order_by('-rank_score','-created_at')
    #dataII = set(data)
    most_vied_stories = Article.objects.all().order_by('-rank_score')[:8]

    paginator = Paginator(data, 5)

    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    HASH[:] = []

    for trend in data:
        result = trends(trend.body)
        if result not in HASH:
            trend = HASH.append(sort(result))

    #trend = set(HASH)
    args = {}
    args.update(csrf(request))
    args['articles'] = results
    args['trends'] = set(HASH[:5])

    args['most_vied_stories'] = most_vied_stories

    return render_to_response('articles.html',args)




def article(request, article_id=1):
    try:
        data = Article.objects.get(id=article_id)
        comments = Comments.objects.filter(article_id=article_id).order_by('-created_at')
        views = data.views
        data.views = views + 1
        data.save()
    except ObjectDoesNotExist:
        data = None
    args = {}
    args.update(csrf(request))
    args['article'] = data
    args['comments'] = comments

    return render_to_response('article.html',args)

def create(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response("create_article.html",args)

def likes(request,article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        like = a.likes
        a.likes = like + 1
        a.save()
        return HttpResponseRedirect("/story/"+article_id+"/")


def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ""

    article = Article.objects.filter(title__contains=search_text)

    args = {}
    args.update(csrf(request))
    args['articles'] = article

    return render_to_response('search.html',args, context_instance=RequestContext(request))


#Email subscription form
def email_subscribe(request):
    if request.POST:
        email = request.POST['email']
        if email_re.match(email):
            try:
                sub = Subscription.objects.get(email=email)
                if sub is not None:
                    return HttpResponse("Email already exits")
            except ObjectDoesNotExist:
                sub = Subscription.create(email)
                sub.save()
            return HttpResponse("Subscription successful")
        else:
            return HttpResponse("Invalid Email")


#Comments
def add_comment(request,article_id):
    p = request.POST
    args = {}
    if p.has_key("body") and p["body"]:
        comment = Comments(article_id=article_id,body=p['body'])
        comment.save()
    elif p["body"] == "":
        args['error'] = "Please enter a comment"

    args.update(csrf(request))
    return HttpResponseRedirect("/story/"+article_id+"/", args)

#@login_required()
class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user_details.html"

    #@login_required()
    def get_object(self, queryset=None):
        user = super(UserProfileDetailView,self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user


def custom_login(request, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/', **kwargs)
    else:
        return HttpResponseRedirect(request, **kwargs)

