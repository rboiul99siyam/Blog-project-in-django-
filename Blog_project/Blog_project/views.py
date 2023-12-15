from django.shortcuts import render
from posts.models import Post
from catagories.models import Catagory
def home(request, category_slug = None):
    data = Post.objects.all() 
    if category_slug is not None:
        category = Catagory.objects.get(slug = category_slug) 
        data = Post.objects.filter(catagroy  = category) 
    categories = Catagory.objects.all() 
    return render(request, 'home.html', {'data' : data, 'category' : categories})