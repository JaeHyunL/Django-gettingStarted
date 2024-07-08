from django.urls import path

from . import views as inventory_views

app_name = "inventory"

urlpatterns = [
    path("", inventory_views.MainView.as_view(), name="main"),
    path("car/", inventory_views.CarFormView.as_view(), name="car"),
]
