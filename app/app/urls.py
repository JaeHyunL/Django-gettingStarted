"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

# from dealershop import views as delar_views
from inventory import views as inventory_views
from polls import views as polls_views

app_name = "polls"

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("inventory/", include("inventory.urls")),
    path("admin/", admin.site.urls),
    path("", polls_views.index),
    # /polls/survey/로 접속했을 때, views.survey 함수를 실행하도록 설정
    path("polls/survey/", polls_views.survey, name="survey"),
    path("polls/thanks/", polls_views.thanks, name="thanks"),
    # path("inventory/", inventory_views.MainView.as_view(), name="main"),
]

handler404 = "app.views.error_404_view"
