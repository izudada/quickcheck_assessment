from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, TemplateView, UpdateView)
                                  
from news.models import Comment, News
import requests


class Index(ListView):
    model = News
    template_name = 'index.html'
    fields = []

    def get_context_data(self):
        context = self.model.objects.all()
        return {'context': context}


class Article(DetailView):
    model = News
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = {}
        article = News.objects.get(id=self.kwargs["pk"])
        context['article'] = article

        comments = article.get_comments()
        context['comments'] = comments
        
        return context


def get_comments(request):
    if request.is_ajax():
        news_id = request.GET.get('id');
        article = News.objects.get(id=news_id)
        comments = article.get_comments()
        commment_holder = {}
        comment_array = []
        data = {}
        for comment in comments:
            commment_holder['author'] = comment.author
            commment_holder['text'] = comment.text
            commment_holder['type'] = comment.type
            commment_holder['hacker_comment_id'] = comment.hacker_comment_id
            commment_holder['date_created'] = comment.date_created
            comment_array.append(commment_holder)
        data['comments'] = comment_array
        return JsonResponse(data)
