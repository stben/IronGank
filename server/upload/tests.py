from django.test import TestCase

# Create your tests here.


class UploadTest(TestCase):
    def test_redirects_after_POST(self):
        response = self.client.post('/upload/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/admin/auth/user/add/')

    def test_upload_no_file(self):
        response = self.client.post('/upload/')
        self.assertTrue(self.client.session['message'], 'Upload error!')
