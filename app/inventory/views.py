from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone


from inventory.models import Car
from inventory.forms import CarForm


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


class CarCreateView(CreateView):
    model = Car
    fields = ["brand", "model", "color", "year"]
    success_url = reverse_lazy("inventory:main")
    # template_name = "inventory/car_basic_form.html"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class CarListView(ListView):
    model = Car
    paginate_by = 100

    queryset = Car.objects.all()

    def get_context_data(self, **kwargs: reverse_lazy) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class CarDetailView(DetailView):
    model = Car


class CarUpdateView(UpdateView):
    model = Car
    fields = ["brand", "model", "color", "year"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("inventory:car-list")


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy("inventory:car-list")
    template_name_suffix = "_confirm_delete"
