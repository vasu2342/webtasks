from .models import Router
from rest_framework.serializers import ModelSerializer
class RouterSerializer(ModelSerializer):
    class Meta:
        model=Router
        fields='__all__'
        extra_kwargs = {
            'url': {'lookup_field': 'sapid'}
        }