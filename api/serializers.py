from rest_framework import serializers
from .models import News

class newsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'