from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import ToDOModel
from django.urls import reverse_lazy


# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    model = ToDOModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = ToDOModel


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = ToDOModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = ToDOModel
    success_url = reverse_lazy('list')


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = ToDOModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
