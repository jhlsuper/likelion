
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#django rest framework -> router -> url  라우터를 통해서 url 를 지정  

router = DefaultRouter()
router.register('post',views.PostviewSet)


urlpatterns =[
    path('',include(router.urls)),

]