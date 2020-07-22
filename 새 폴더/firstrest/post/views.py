from rest_framework import viewsets
#데이터 처리 대상
from .models import Post
from .serializer import PostSerializer
# status에 따라 직업 response를 처리할 것 
from django.http import Http404  #get objec 404직접 구현
from rest_framework.response import Response
from rest_framework import status
#Apiviews를 상속받은 CBV
from rest_framework.views import APIView
#PostDetail 클래스의 get_object 메소드 대신 이거 써도 된다 
#from django.shortcuts import get_object_or_404
#CBV 

class PostList(ApiView):
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True) #쿼리셋 넘기기 many = true인자
        return Response(serializer.data) #직접 response리턴해주기
        
    def post(self, request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    