# Create your views here.
from dblog.models import Article
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def detail(request, article_id):
    c = {}
    c.update(csrf(request))
    a = get_object_or_404(Article, pk=article_id)
    return render(request, 'article/detail.html', {'article' : a})
