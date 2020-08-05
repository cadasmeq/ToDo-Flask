from flask_testing import TestCase
from main import app
from flask import current_app, url_for

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app
    
    def test_app_exits(self):
        self.assertIsNotNone(current_app)
    
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
        
    def test_index_redirects(self):
        response = self.client.get(url_for('home'))
        self.assertRedirects(response, url_for('myIP'))
    
    def test_myip_get(self):
        response = self.client.get(url_for('myIP'))
        self.assert200(response)
    
    def test_myip_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake_password',
        }
        
        response = self.client.post(url_for('myIP'), data=fake_form)

        #import pdb; pdb.set_trace()
        self.assertRedirects(response, url_for('home'))

