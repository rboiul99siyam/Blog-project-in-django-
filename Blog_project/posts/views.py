from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from . import forms
from . import models
# Create your views here.

@login_required
def add_post(res):
    if res.method == 'POST':
        post_form = forms.Add_post(res.POST)
        if post_form.is_valid():
            post_form.instance.Author = res.user
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.Add_post()
    return render(res,'add_post.html',{'form':post_form})

@login_required
def Edit_post(res,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.Add_post(instance=post)
    if res.method == "POST":
        post_form = forms.Add_post(res.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.Author = res.user
            post_form.save()
            return redirect('homePage')
    else:
        post_form = forms.Add_post(instance=post)
    return render(res,'add_post.html',{'form':post_form})

def delete_post(res,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homePage')


