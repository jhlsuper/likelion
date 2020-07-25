
from django.contrib import admin
from django.urls import path, include
import post.urls
from userpost import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/',include('post.urls')),
    path('userpost/',include('userpost.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
