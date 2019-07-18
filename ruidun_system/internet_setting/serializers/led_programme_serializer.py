import uuid

from rest_framework import serializers

from ..models import LedProgramme


class LedProgrammeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LedProgramme
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False},
        }

    def create(self, validated_data):
        """新建"""
        validated_data['id'] = uuid.uuid4()
        return LedProgramme.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.name = validated_data.get('name', instance.name)
        instance.w_x = validated_data.get('w_x', instance.w_x)
        instance.h_y = validated_data.get('h_y', instance.h_y)
        instance.font_name = validated_data.get('font_name', instance.font_name)
        instance.font_size = validated_data.get('font_size', instance.font_size)
        instance.font_bold = validated_data.get('font_bold', instance.font_bold)
        instance.x_align = validated_data.get('x_align', instance.x_align)
        instance.y_align = validated_data.get('y_align', instance.y_align)
        instance.font_stunt = validated_data.get('font_stunt', instance.font_stunt)
        instance.font_showtime = validated_data.get('font_showtime', instance.font_showtime)
        instance.font_run = validated_data.get('font_run', instance.font_run)
        instance.save()
        return instance
