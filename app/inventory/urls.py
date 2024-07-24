from django.urls import path
from django.views.generic.base import RedirectView
from .greet import greeting
from . import views as inventory_views

app_name = "inventory"

urlpatterns = [
    path("", inventory_views.MainView.as_view(), name="main"),
    path("car/", inventory_views.CarFormView.as_view(), name="car"),
    path(
        "create_car/",  # noqa
        inventory_views.CarCreateView.as_view(),  # noqa
        name="car-create",  # noqa
    ),  # noqa
    path("list_car/", inventory_views.CarListView.as_view(), name="car-list"),
    path(
        "detail_car/<int:pk>",
        inventory_views.CarDetailView.as_view(),
        name="car-detail",
    ),
    path(
        "update_car/<int:pk>",
        inventory_views.CarUpdateView.as_view(),
        name="car-update",
    ),
    path(
        "delete_car/<int:pk>",
        inventory_views.CarDeleteView.as_view(),
        name="car-delete",
    ),
    path("", RedirectView.as_view(url="/inventory")),
    path("fbv", inventory_views.fbv_view, name="fbv"),
    path("greeting/", greeting, name="greeting"),
]
