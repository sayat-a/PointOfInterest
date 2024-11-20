from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from poi.poi_api.models import PointOfInterest
from poi.poi_api.serializers import PointOfInterestSerializer


# Create your views here.
class PointOfInterestViewSet(ModelViewSet):
    queryset = PointOfInterest.objects.all()  # Все записи из таблицы
    serializer_class = PointOfInterestSerializer  # Указали наш сериализатор
    filter_backends = [SearchFilter]  # Возможность фильтрации
    search_fields = ['category']  # Разрешаем фильтрацию по категории

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():  # Проверяем данные на корректность
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()  # Получаем объект из базы по ID.
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial
        )
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
