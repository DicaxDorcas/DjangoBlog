from django.test import TestCase
from project.models import Project

class ProjectViewsTestCase(TestCase):
    fixtures = ['project_views_testdata.json']
    def test_index(self):
        resp = self.client.get('/projects/')
        self.assertEqual(resp.status_code, 200)

    def test_detail(self):
        resp = self.client.get('/projects/1/')
        self.assertEqual(resp.status_code, 200)
        
        resp2 = self.client.get('/projects/1000/')
        self.assertEqual(resp2.status_code, 404) 

