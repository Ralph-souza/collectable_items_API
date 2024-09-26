from rest_framework import serializers

from drf_jsonmask.serializers import FieldsListSerializerMixin

from .models import (
    UserModel,
    LoanerModel,
    ItemImageModel,
    ItemModel,
    LoanHistoryModel
)


class UserSerializer(FieldsListSerializerMixin, serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%H:%M - %d/%m?%Y")
    updated_at = serializers.DateTimeField(format="%H:%M - %d/%m?%Y")

    class Meta:
        model = UserModel
        fields = "__all__"
        read_only_fields = ("id", "created_at")


class LoanerSerializer(FieldsListSerializerMixin, serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%H:%M - %d/%m?%Y")
    updated_at = serializers.DateTimeField(format="%H:%M - %d/%m?%Y")

    class Meta:
        model = LoanerModel
        fields = "__all__"
        read_only_fields = ("id", "created_at")


class ItemImageSerializer(FieldsListSerializerMixin, serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%H:%M - %d/%m?%Y")
    updated_at = serializers.DateTimeField(format="%H:%M - %d/%m?%Y")

    class Meta:
        model = ItemImageModel
        fields = "__all__"
        read_only_fields = ("id", "created_at")


class ItemSerializer(FieldsListSerializerMixin, serializers.ModelSerializer):
    loan_date = serializers.DateField(format="%d/%m?%Y")
    return_date = serializers.DateField(format="%d/%m?%Y")
    created_at = serializers.DateTimeField(format="%H:%M - %d/%m?%Y")
    updated_at = serializers.DateTimeField(format="%H:%M - %d/%m?%Y")

    class Meta:
        model = ItemModel
        fields = "__all__"
        read_only_fields = ("owner", "id", "created_at")


class LoanHistory(FieldsListSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = LoanHistoryModel
        fields = "__all__"
        read_only_fields = ("item", "loaner", "loan_date", "return_date")
