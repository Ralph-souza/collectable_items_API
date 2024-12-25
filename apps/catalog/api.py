import uuid

from drf_jsonmask.views import OptimizedQuerySetMixin

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError

from django.shortcuts import get_object_or_404

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
    

class UserDeleteApiView(OptimizedQuerySetMixin, APIView):
    queryset = UserModel.objects.all()
    serializer = UserSerializer

    def delete(self, request, *args, **kwargs):
        user = UserModel.objects.get(pk=kwargs.get("id"))
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoanerViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = LoanerModel.objects.all().order_by("created_at")
    serializer_class = LoanerSerializer


class ItemImageViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = ItemImageModel.objects.all().order_by("created_at")
    serializer_class = ItemImageSerializer


class ItemViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = ItemModel.objects.all().order_by("created_at")
    serializer_class = ItemSerializer


class ItemCreateApiView(OptimizedQuerySetMixin, APIView):
    queryset = ItemModel.objects.all()
    serializer = ItemSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        user = data.get("owner")
        if not user:
            raise ValidationError({"owner": "O campo proprietário é obrigatório!"})

        try:
            user_uuid = uuid.UUID(user)
        except ValueError:
            raise ValidationError({"owner": "O ID fornecido não é um UUID válido!"})

        owner = get_object_or_404(UserModel, pk=user_uuid)

        title = data.get("title")
        if not title:
            raise ValidationError({"title": "O campo título é obrigatório!"})

        image_url = data.get("image")
        if not image_url:
            raise ValidationError({"image": "O campo imagem é obrigatório!"})

        image, _ = ItemImageModel.objects.get_or_create(url=image_url)

        category = data.get("category")
        if not category:
            raise ValidationError({"category": "O campo categoria é obrigatório!"})

        main_actor = data.get("main_actor")
        author = data.get("author")

        if category in ["books", "comics", "action_figures"]:
            if not author:
                raise ValidationError({"author": "O campo autor é obrigatório!"})
        if category in ["movies", "games"]:
            if not main_actor:
                raise ValidationError({"main_actor": "O campo ator principal é obrigatório!"})
            
        platform = data.get("platform")
        media_type = data.get("media_type")
        launch_date = data.get("launch_date")
        item_status = data.get("status")

        item_data = {
            "owner": owner.id,
            "title": title,
            "image": image.id,
            "category": category,
            "main_actor": main_actor,
            "author": author,
            "platform": platform,
            "media_type": media_type,
            "launch_date": launch_date,
            "status": item_status,
        }

        serializer = ItemSerializer(data=item_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = LoanModel.objects.all().order_by("loan_date")
    serializer_class = LoanSerializer


class LoanHistoryViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = LoanHistoryModel.objects.all().order_by("-loan__loan_date")
    serializer_class = LoanHistorySerializer
