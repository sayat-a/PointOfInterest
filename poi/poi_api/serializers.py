from rest_framework import serializers
from poi.poi_api.models import PointOfInterest


# Создаем сериализатор для преобразования в JSON и обратно
class PointOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfInterest
        fields = '__all__'  # Берем все поля из модели.

# Вводим валидацию для координат на нахождение их в пределах допустимых значений
    def validate_latitude(self, value):
        if not (-90 <= value <= 90):
            raise serializers.ValidationError(
                "Широта должна быть в пределах -90 до 90."
            )
        return value

    def validate_longitude(self, value):
        if not (-180 <= value <= 180):
            raise serializers.ValidationError(
                "Долгота должна быть в пределах -180 до 180."
            )
        return value
