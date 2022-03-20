from rest_framework.test import APITestCase


class CarAPIViewTest(APITestCase):
    def setUp(self):
        self.client.post('/cars/', {'make': 'HONDA', 'model': 'Civic'})

    def test_car_list(self):
        response = self.client.get('/cars/')
        self.assertEqual(response.status_code, 200)

    def test_car_detail(self):
        response = self.client.get('/cars/1/')
        self.assertEqual(response.status_code, 200)

    def test_car_create(self):
        response = self.client.post('/cars/', {'make': 'HONDA', 'model': 'CR-V'})
        self.assertEqual(response.status_code, 201)

    def test_car_update(self):
        response = self.client.put('/cars/1/', {'make': 'HONDA', 'model': 'Civic'})
        self.assertEqual(response.status_code, 200)

    def test_car_delete(self):
        response = self.client.delete('/cars/1/')
        self.assertEqual(response.status_code, 204)


class RateCarsAPIViewTest(APITestCase):
    def setUp(self):
        self.client.post('/cars/', {'make': 'HONDA', 'model': 'CR-V'})
        self.client.post('/rate/', {'car_id': 1, 'rating': 5})
        self.client.post('/rate/', {'car_id': 1, 'rating': 4})

    def test_car_rating(self):
        response = self.client.post('/rate/', {'car_id': 1, 'rating': 3})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['rating'], 3)

    def test_car_rating_average(self):
        response = self.client.get('/cars/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['avg_rating'], 4.5)


class PopularCarsAPIView(APITestCase):
    models = ['Civic', 'CR-V', 'Accord']

    def setUp(self):
        for i, model in enumerate(self.models):
            self.client.post('/cars/', {'make': 'HONDA', 'model': model})
            for _ in range(i + 1):
                self.client.post('/rate/', {'car_id': i + 1, 'rating': i + 1})

    def test_popular_cars(self):
        response = self.client.get('/popular/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['model'], self.models[2])
        self.assertEqual(response.data[1]['model'], self.models[1])
        self.assertEqual(response.data[2]['model'], self.models[0])
