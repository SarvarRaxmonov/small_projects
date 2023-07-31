from rest_framework import serializers
from rest_framework.serializers import Serializer

from rest_uz.models import Todo


class MovieSerializer(Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    desc = serializers.CharField()
    is_active = serializers.BooleanField(read_only=True)

class TodoSerializer(Serializer):
    task = serializers.CharField()
    class Meta:
        model = Todo
        fields = ("task",)

    def create(self, validated_data):
        data = Todo.objects.create(**validated_data)
        data.save()
        return data

