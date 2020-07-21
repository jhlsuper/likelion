from django.db import models

class ClassBlog(models.Model):
    title = models.Charfield(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = modles.DateTImeField(auto_now=True)
    body = modles.TextField()

def _str_(self):
    return self.title 
