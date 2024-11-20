from rest_framework.routers import DefaultRouter
from poi.poi_api.views import PointOfInterestViewSet


router = DefaultRouter()  # Роутер для автоматической генерации маршрутов.
router.register(r'poi', PointOfInterestViewSet)  # Подключаем ViewSet.
urlpatterns = router.urls  # Генерируем список маршрутов.
