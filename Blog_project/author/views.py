from django.shortcuts import render, redirect
from . import forms
# Create your views here.

def add_author(res):
    if res.method == 'POST':
        author_form = forms.Add_author(res.POST)
        if author_form.is_valid():
            author_form.save()
            print(author_form.cleaned_data)
            return redirect('add_author')
    
    else:
        author_form = forms.Add_author()
    return render(res, 'add_author.html', {'form' : author_form})