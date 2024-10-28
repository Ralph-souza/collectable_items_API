from django.urls import include, re_path

urlpatterns = [
    re_path(r"^v1/api/", include("apps.catalog.urls")),
]
