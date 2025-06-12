import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<form', response.get_data(as_text=True))

    def test_volume_calculation(self):
        response = self.app.post('/', data={
            'length': '2',
            'width': '3',
            'height': '4'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('24.0', response.get_data(as_text=True))

    def test_invalid_input(self):
        response = self.app.post('/', data={
            'length': 'abc',
            'width': '3',
            'height': '4'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ошибка', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()

