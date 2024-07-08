from django.http import HttpResponse
from django.views import View
from inventory.forms import CarForm
from django.views.generic import TemplateView, FormView


# 이러한 방식을 CBV Class Based View라고 한다.
class MainView(TemplateView):
    template_name = "inventory/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Hello, World!"
        return context


class CarFormView(FormView):
    template_name = "inventory/car_basic_form.html"
    form_class = CarForm

    # Class Base Viedw 에선 evluated가 함수를 import할 때 로드 됨
    # 따라서 아래처럼 쓰거나 lazy_reverse를 써서 로딩할 것.
    success_url = "/inventory"
