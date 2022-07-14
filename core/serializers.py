from.models import producto
from rest_framework import serializers

class producto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'
