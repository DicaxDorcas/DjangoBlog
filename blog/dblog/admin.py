from dblog.models import Article, Comments
from django.contrib import admin




class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
