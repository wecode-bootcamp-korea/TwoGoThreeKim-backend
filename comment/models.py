from django.db import models

class Comment(models.Model):
    user_id = models.CharField(max_length=100)
    user_comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'


