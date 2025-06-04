from rest_framework import serializers
from .models import FAQs


class FAQSerialiser(serializers.ModelSerializer):
    class Meta:
        model = FAQs
        fields = "__all__"
        read_only_fields = ['id']