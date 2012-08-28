# Create your views here.
from dblog.models import Article
import django.http as http
from django.core.cache import cache
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from recaptcha_works.decorators import fix_recaptcha_remote_ip
from tagging.models import Tag, TaggedItem

def tags(request):
    return render_to_response("article/tags/tags.html")

def with_tag(request, tag, object_id=None, page=1):
    cache_key = 'with_tag_view_cache'
    cache_time = 1800
    result = cache.get(cache_key)
    if not result:
        query_tag = Tag.objects.get(name=tag)
        articles = TaggedItem.objects.get_by_model(Article, query_tag)
        articles = articles.order_by('-pub_date')
        result = render_to_response("article/tags/with_tag.html", dict(tag=tag, articles=articles)) 
        cache.set(cache_key, result, cache_time)
    return result  

def index(request):
    latest_article_list = Article.objects.all().order_by('-pub_date')
    paginator = Paginator(latest_article_list, 4, allow_empty_first_page=True)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render_to_response('article/index.html', {'articles' : articles})

@fix_recaptcha_remote_ip
def detail(request, slug, article_id):
    a = get_object_or_404(Article, pk=article_id)
    return render(request, 'article/detail.html', {'article' : a})
