from django.urls import path

from kitchen.views import index, CookListView


urlpatterns = [
    path("", index, name="index"),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cooks-list",
    ),
    ]

app_name = "kitchen"
