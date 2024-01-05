from .models import ToDo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class TodoListView(ListView):
    model = ToDo
    template_name = "todos/todo_list.html"


class TodoCreateView(CreateView):
    model = ToDo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    template_name = "todos/todo_form.html"


class TodoUpdateView(UpdateView):
    model = ToDo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = ToDo
    success_url = reverse_lazy("todo_list")
