from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    #评论时间自动生成
    created_time = models.DateTimeField(auto_now_add=True)

    #评论关联文章
    post = models.ForeignKey('image.Post',on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]