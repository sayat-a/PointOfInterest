from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from poi.poi_api.models import PointOfInterest


# Тесты на добавление валидных точек
class PointOfInterestTests(TestCase):
    def setUp(self):
        """Создаем фикстуры"""
        PointOfInterest.objects.create(
            name="Парк 1",
            description="Прекрасный парк",
            latitude=51.128000,
            longitude=71.430000,
            category="парк"
        )
        PointOfInterest.objects.create(
            name="Парк 2",
            description="Еще один парк",
            latitude=51.128001,
            longitude=71.430001,
            category="парк"
        )
        PointOfInterest.objects.create(
            name="Ресторан 1",
            description="Лучший ресторан",
            latitude=51.128002,
            longitude=71.430002,
            category="ресторан"
        )

    def test_get_all_points(self):
        """Тест получения всех точек"""
        response = self.client.get(reverse('pointofinterest-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_point_by_id(self):
        """Тест получения точки по ID"""
        response = self.client.get(reverse('pointofinterest-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Парк 1")

    def test_filter_points_by_category(self):
        """Тест фильтрации точек по категории"""
        response = self.client.get(
            reverse('pointofinterest-list'), {'search': 'парк'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


# Тесты для обновления точки (полного и частичного)
class PointUpdateTests(TestCase):
    def setUp(self):
        self.point = PointOfInterest.objects.create(
            name="Ресторан 2",
            description="Хороший ресторан",
            latitude=51.128000,
            longitude=71.430000,
            category="ресторан"
        )

    def test_full_update(self):
        """Тест полного обновления точки"""
        updated_data = {
            "name": "Обновленный Ресторан",
            "description": "Теперь лучше!",
            "latitude": 51.128001,
            "longitude": 71.430001,
            "category": "ресторан"
        }
        response = self.client.put(
            reverse('pointofinterest-detail', args=[self.point.id]),
            updated_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Обновленный Ресторан")

    def test_partial_update(self):
        """Тест частичного обновления точки"""
        updated_data = {"description": "Новый комментарий"}
        response = self.client.patch(
            reverse('pointofinterest-detail', args=[self.point.id]),
            updated_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], "Новый комментарий")


# Тест на удаление точки
class PointDeleteTests(TestCase):
    def setUp(self):
        self.point = PointOfInterest.objects.create(
            name="Удаляемый Ресторан",
            description="Будет удален",
            latitude=51.128000,
            longitude=71.430000,
            category="ресторан"
        )

    def test_delete_point(self):
        """Тест удаления точки"""
        response = self.client.delete(
            reverse('pointofinterest-detail', args=[self.point.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Проверяем, что точка удалена
        response = self.client.get(
            reverse('pointofinterest-detail', args=[self.point.id])
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# Тест добавления точки с неверными координатами
class InvalidPointTests(TestCase):
    def test_invalid_latitude(self):
        """Тест добавления точки с неверной широтой"""
        invalid_data = {
            "name": "Неверная широта",
            "description": "Широта за пределами",
            "latitude": 100,
            "longitude": 71.430000,
            "category": "парк"
        }
        response = self.client.post(
            reverse('pointofinterest-list'),
            invalid_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_longitude(self):
        """Тест добавления точки с неверной долготой"""
        invalid_data = {
            "name": "Неверная долгота",
            "description": "Долгота за пределами",
            "latitude": 51.128000,
            "longitude": 200,
            "category": "парк"
        }
        response = self.client.post(
            reverse('pointofinterest-list'),
            invalid_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_latitude_and_longitude(self):
        """Тест добавления точки с неверными широтой и долготой"""
        invalid_data = {
            "name": "Неверные координаты",
            "description": "И широта, и долгота неверны",
            "latitude": -100,
            "longitude": -200,
            "category": "парк"
        }
        response = self.client.post(
            reverse('pointofinterest-list'),
            invalid_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
