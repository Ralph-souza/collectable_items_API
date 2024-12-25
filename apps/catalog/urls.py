from django.urls import path

from rest_framework import routers

from .api import (
    UserViewSet,
    UserCreateApiView,
    UserUpdateApiView,
    UserDeleteApiView,
    LoanerViewSet,
    ItemImageViewSet,
    ItemViewSet,
    ItemCreateApiView,
    LoanViewSet,
    LoanHistoryViewSet
)


app_name = "catalog"

router = routers.DefaultRouter()
router.register(r"get_user", UserViewSet, basename="get_user")
router.register(r"loaner", LoanerViewSet, basename="loaner")
router.register(r"item_image", ItemImageViewSet, basename="item_image")
router.register(r"item", ItemViewSet, basename="item")
router.register(r"loan", LoanViewSet, basename="loan")
router.register(r"loan_history", LoanHistoryViewSet, basename="loan_history")

urlpatterns = [
    path(r"user/create/", UserCreateApiView.as_view(), name="user_create"),
    path(r"user/update/put/<uuid:id>/", UserUpdateApiView.as_view(), name="user_update_put"),
    path(r"user/update/patch/<uuid:id>/", UserUpdateApiView.as_view(), name="user_update_patch"),
    path(r"user/delete/<uuid:id>/", UserDeleteApiView.as_view(), name="user_delete"),
    path(r"item/create/", ItemCreateApiView.as_view(), name="item_create"),
]

urlpatterns += router.urls
