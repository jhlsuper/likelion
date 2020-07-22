
from django.contrib import admin
from django.urls import path, include
import post.urls
from userpost import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('post.urls')),
    path('userpost',include('userpost.urls')),
]
