import uuid
from rest_framework import serializers
from staff.models import Trades


class TradesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trades
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False},
            "colour": {"required": False}
        }

    def create(self, validated_data):
        """新建"""
        return Trades.objects.create(pk=uuid.uuid4(), **validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""

        instance.trades_name = validated_data.get('trades_name', instance.trades_name)
        instance.colour = validated_data.get('colour', instance.colour)
        instance.index = validated_data.get('index', instance.index)
        instance.is_used = validated_data.get('is_used', instance.is_used)
        instance.save()
        return instance