from .models import Module, Enrollment
from users.models import User
from rest_framework import serializers


class ModuleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"


class UserReadOnlySerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email")
        read_only_fields = ("id", "email")


class EnrollmentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"