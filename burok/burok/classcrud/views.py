from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClassBlog
from django.urls import reverse_lazy
# Create your views here.

class BlogView(ListView):  # html 템플릿 : 블로그 리스트를 담은 html (소문자모델)_list.html 
    model = ClassBlog

class BlogCreate(CreateView):  # html : form (입력공간을 가지고있는 html) (소문자모델)_form.html
    model = ClassBlog
    fields = ['title','body']
    success_url = reverse_lazy('list')

class BlogDetail(DetailView):   #  html 상세 페이지를 담은 html  (소문자모델)_detail.html 
    model = ClassBlog
    

class BlogUpdate(UpdateView):  # 입력공간을 갖고있는 html  (소문자모델)_form.html
    model = ClassBlog 
    model = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):  # html : "이거 진짜로 지울거야?"  (소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list') 