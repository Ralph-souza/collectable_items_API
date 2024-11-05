from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import viewsets

from .models import (
    UserModel,
    LoanerModel,
    ItemImageModel,
    ItemModel,
    LoanModel,
    LoanHistoryModel
)

from .serializers import (
    UserSerializer,
    LoanerSerializer,
    ItemImageSerializer,
    ItemSerializer,
    LoanSerializer,
    LoanHistorySerializer
)


class UserViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = UserModel.objects.all().order_by("created_at")
    serializer_class = UserSerializer


class LoanerViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = LoanerModel.objects.all().order_by("created_at")
    serializer_class = LoanerSerializer


class ItemImageViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = ItemImageModel.objects.all().order_by("created_at")
    serializer_class = ItemImageSerializer


class ItemViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = ItemModel.objects.all().order_by("created_at")
    serializer_class = ItemSerializer


class LoanViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = LoanModel.objects.all().order_by("loan_date")
    serializer_class = LoanSerializer


class LoanHistoryViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = LoanHistoryModel.objects.all().order_by("-return_date")
    serializer_class = LoanHistorySerializer
