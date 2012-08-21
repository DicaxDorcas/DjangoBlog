from django.test import TestCase
from dblog.models import Article

class DblogViewsTestCase(TestCase):
    def test_index(self):
        post_1 = Article.objects.create(
            title='DjangoTest',
            content='DjangoTest',
            author='DjangoTest',
            tags='test,test,'
        )
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('articles' in resp.context)
        self.assertEqual([article.pk for article in resp.context['latest_article_list']], [1])
