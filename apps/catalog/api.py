from drf_jsonmask.views import OptimizedQuerySetMixin

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

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
    http_method_names = ["get"]
    queryset = UserModel.objects.all().order_by("created_at")
    serializer_class = UserSerializer


class UserCreateApiView(OptimizedQuerySetMixin, APIView):
    queryset = UserModel.objects.all().order_by("created_at")
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserUpdateApiView(OptimizedQuerySetMixin, APIView):
    queryset = UserModel.objects.all().order_by("created_at")
    serializer_class = UserSerializer

    def get_user(self, id):
        try:
            return UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            raise NotFound(detail="User not found", code=status.HTTP_404_NOT_FOUND)      

    def put(self, request, *args, **kwargs):
        user = self.get_user(kwargs.get("id"))
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, *args, **kwargs):
        user = self.get_user(kwargs.get("id"))
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    queryset = LoanHistoryModel.objects.all().order_by("-loan__loan_date")
    serializer_class = LoanHistorySerializer
