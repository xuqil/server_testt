from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment#对应的数据库模型
        fields = ['name','email','url','text']