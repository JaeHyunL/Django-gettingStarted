from django.urls import reverse, reverse_lazy

# todo_list/todo_app/views.py
from typing import Any
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import ToDoList, ToDoItem


class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"


class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context


class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new List"
        return context


class ItemCreate(CreateView):
    model = ToDoItem
    fields = ["todo_list", "title", "description", "due_date"]

    def get_initial(self) -> dict[str, Any]:
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new Item"
        return context

    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.todo_list.id])


class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = ["todo_list", "title", "description", "due_date"]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit Item"
        return context

    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.todo_list.id])


class ListDelete(DeleteView):
    model = ToDoList

    success_url = reverse_lazy("index")


class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self) -> str:
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context
