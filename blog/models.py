from django.db import models
from datetime import datetime

class TimestampableMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        
        
class Blog(TimestampableMixin):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.CharField(max_length=120)
    post_date = models.DateTimeField(default=datetime.now())