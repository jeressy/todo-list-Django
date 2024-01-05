from .models import ToDo
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TodoListView(ListView):
    model = ToDo
    template_name = "todos/todo_list.html"


class TodoCreateView(CreateView):
    model = ToDo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    template_name = "todos/todo_form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        helper = FormHelper()
        helper.add_input(Submit("submit", "Salvar"))
        form.helper = helper
        return form
