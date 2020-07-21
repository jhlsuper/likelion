
from django.contrib import admin
from django.urls import path
import classcrud.urls
import classcrud.views
urlpatterns = [
    path('admin/', admin.site.urls),
]