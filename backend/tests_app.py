import unittest
from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_register_endpoint(self):
        response = self.app.post('/register', json={
            'username': 'test_user',
            'password': 'password123',
            'role': 'user'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration successful'    , response.data)

    def test_login_endpoint(self):
        # Register a user before attempting to log in
        self.app.post('/register', json={
            'username': 'test_user',
            'password': 'password123',
            'role': 'user'
        })

        response = self.app.post('/login', json={
            'username': 'test_user',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful', response.data)

    def test_add_post_endpoint(self):
        # First, add a topic for the post
        self.app.post('/add-topic', json={
            'content': 'Test Topic'
        })

        response = self.app.post('/add-post', json={
            'topic': 'Test Topic',
            'content': 'Test Content'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Post added successfully', response.data)


if __name__ == '__main__':
    unittest.main()
