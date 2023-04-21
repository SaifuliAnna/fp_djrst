import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# 3______________
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()


# 4_____________-

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validate_data):
        return Women.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get("title", instance.title)
        instance.content = validate_data.get("content", instance.content)
        instance.time_update = validate_data.get("time_update", instance.time_update)
        instance.is_published = validate_data.get("is_published", instance.is_published)
        instance.cat_id = validate_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance
