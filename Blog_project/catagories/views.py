from django.shortcuts import render,redirect

from . import forms

def add_catagory(res):
    if res.method == 'POST':
        catagory_form = forms.CatagoryForm(res.POST)
        if catagory_form.is_valid():
            catagory_form.save()
            return redirect('add_catagory')
    else:
        catagory_form = forms.CatagoryForm()
    return render(res,'add_catagory.html',{'form':catagory_form})
