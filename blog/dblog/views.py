# Create your views here.
from dblog.models import Article
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    latest_article_list = Article.objects.all().order_by("-pub_date")[:5]
    return render_to_response('article/index.html', {'latest_article_list' : latest_article_list})

def detail(request, article_id):
    a = get_object_or_404(Article, pk=article_id)
    return render_to_response('article/detail.html', {'article' : a})
