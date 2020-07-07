from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'home.html',{'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id) ##pk 는 검색조건
    return render(request, 'detail.html',{'details':details})

def new(request):  #new.html을 띄어주는 함수
    return render(request, 'new.html')

def create(request):   #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date= timezone.datetime.now() ##작성한 시간
    blog.save()  ##블로그라는 객체에 받은 내용을 데베에 저장하는 것.
    return redirect('/blog/'+str(blog.id))