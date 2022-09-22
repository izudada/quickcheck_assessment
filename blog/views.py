from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, TemplateView, UpdateView)
from news.models import Comment, News
import requests


class Index(ListView):
    model = News
    template_name = 'index.html'
    fields = []

    def get_queryset(self):
        url = "http://127.0.0.1:8000/api/v0/items/all"
        response = requests.get(url)
        result = response.json()
        print(result)
        return result
