import uuid

from rest_framework import serializers

from internet_setting.models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        exclude = ("is_used",)
        extra_kwargs = {
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        pk = uuid.uuid4()
        return Music.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        instance.note = validated_data.get("note", instance.note)
        instance.path = validated_data.get("path", instance.path)

        instance.save()
        return instance
