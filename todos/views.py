
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Todo
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect


class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = enumerate(context['object_list'], start=1)
        return context

class TodoCreateView(CreateView):
    model = Todo
    fields = ["titulo","entrega_dt"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["titulo","entrega_dt"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()    
        return redirect("todo_list")