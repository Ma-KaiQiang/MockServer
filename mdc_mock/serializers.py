from rest_framework import serializers
from mdc_mock import models


class MdcMockSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.MdcMockModel
        fields = '__all__'

    createTime = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    updateTime = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # def create(self,validated_data):
    #     print(validated_data)
