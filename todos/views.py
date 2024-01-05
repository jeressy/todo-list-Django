from .models import ToDo
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone



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



class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        todo.finished_at = timezone.now()
        todo.save()
        return redirect("todo_list")