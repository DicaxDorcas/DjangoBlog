from dblog.models import Article, Comments
from django.contrib import admin




class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

admin.site.register(Article, ArticleAdmin)
