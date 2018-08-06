from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags


class Category(models.Model):
    """分类"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """文章类"""
    #标题与主体
    title = models.CharField(max_length=70)
    body = models.TextField()
    #文章创建时间与最后修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #文章摘要
    excerpt = models.CharField(max_length=200,blank=True)
    #文章与分类相关联，一篇文章对应一个类
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    #文章标题，文章标题与文章多对多
    tags = models.ManyToManyField(Tag,blank=True)
    #作者，把文章与作者关联起来
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #阅读量
    views = models.PositiveIntegerField(default=False)


    class Meta:
        #排序顺序
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """获取当前文章链接"""
        return reverse('image:detail',kwargs={'pk':self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args,**kwargs):

        if not self.excerpt:
            self.excerpt = strip_tags(self.body)[:54]

        super(Post,self).save(*args,**kwargs)






