from django.test import TestCase
from dblog.models import Article

class DblogViewsTestCase(TestCase):
    fixtures = ['dblog_views_testdata.json']
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('articles' in resp.context)
        self.assertEqual([article.id for article in resp.context['articles']], [2, 1])

    def test_detail(self):
        resp = self.client.get('/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['article'].id, 1)
        self.assertEqual(resp.context['article'].title, 'sdfsdfsd')
        
        resp2 = self.client.get('/1000/')
        self.assertEqual(resp2.status_code, 404) 

