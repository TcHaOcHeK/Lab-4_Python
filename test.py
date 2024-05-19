import unittest
from app import app

class TestHome(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_get_request(self):
        """Тестирование GET запроса."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Now expecting 200
        self.assertIn('Введите коэффициенты квадратного уравнения:'.encode('utf-8'), response.data)

    def test_post_request_with_two_solution(self):
        """Тестирование POST запроса с уравнением имеющим 2 действительных корня."""
        data = {
            'a': '-1',
            'b': '7',
            'c': '8'
        }
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Корни уравнения: x1 = -1.0, x2 = 8.0'.encode('utf-8'), response.data)

    def test_post_request_with_one_solution(self):
        """Тестирование POST запроса с уравнением имеющим 1 действительный корень."""
        data = {
            'a': '1',
            'b': '4',
            'c': '4'
        }
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Уравнение имеет один корень: x = -2.0'.encode('utf-8'), response.data)

    def test_post_request_with_zero_solution(self):
        """Тестирование POST запроса с уравнением не имеющим действительных корней."""
        data = {
            'a': '1',
            'b': '1',
            'c': '2'
        }
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Уравнение не имеет действительных корней'.encode('utf-8'), response.data)

    def test_post_request_with_line(self):
        """Тестирование POST запроса с линейным уравнением."""
        data = {
            'a': '0',
            'b': '1',
            'c': '2'
        }
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('-2.0'.encode('utf-8'), response.data)

    def test_post_request_with_no_solution(self):
        """Тестирование POST запроса с уравнением которое не имеет решений."""
        data = {
            'a': '0',
            'b': '0',
            'c': '2'
        }
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Не имеет решений'.encode('utf-8'), response.data)

    def test_post_request_with_infinity_solutions(self):
        """Тестирование POST запроса с уравнением которое имеет бесконечное количество решений."""
        data = {
            'a': '0',
            'b': '0',
            'c': '0'
        }
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Бесконечное количество решений'.encode('utf-8'), response.data)

    def test_404_error(self):
        """Тестирование 404 ошибки."""
        response = self.client.get('/nonexistent-route')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
