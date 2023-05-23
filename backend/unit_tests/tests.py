import unittest
from app import app

class BackendTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_register_endpoint(self):
        response = self.app.post('/register', json={
            'username': 'test_user',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Success', response.data)
    
    def test_login_endpoint(self):
        response = self.app.post('/login', json={
            'username': 'test_user',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logged in', response.data)

if __name__ == '__main__':
    unittest.main()