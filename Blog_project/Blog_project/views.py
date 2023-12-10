from django.shortcuts import render
from posts.models import Post
def home(res):
    data = Post.objects.all()
    return render(res,'home.html',{'data':data})