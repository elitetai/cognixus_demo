from rest_framework import serializers
from todo_list.models import Todo

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True)
    is_completed = serializers.BooleanField(required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance