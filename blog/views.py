from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Todo
# Create your views here.

class TodoListView(ListView):
    model = Todo
    template_name = "home.html"
class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo_detail.html"
class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo_new.html"
    fields = ["title","body","author"]
class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "todo_edit.html"
    fields = ["title","body"]
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('home')