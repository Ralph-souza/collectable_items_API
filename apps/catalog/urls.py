from rest_framework import routers

from .api import (
    UserViewSet,
    LoanerViewSet,
    ItemImageViewSet,
    ItemViewSet,
    LoanHistoryViewSet
)


app_name = "catalog"

router = routers.DefaultRouter()
router.register(r"user", UserViewSet, basename="user")
router.register(r"loaner", LoanerViewSet, basename="loaner")
router.register(r"item_image", ItemImageViewSet, basename="item_image")
router.register(r"item", ItemViewSet, basename="item")
router.register(r"loan_history", LoanHistoryViewSet, basename="loan_history")

urlpatterns = router.urls
