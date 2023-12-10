from django.shortcuts import render,redirect

# Create your views here.
from . import forms
def Add_profiles(res):
    if res.method == 'POST':
        profile_form = forms.Add_profile(res.POST)
        if profile_form.is_valid():
            profile_form.save()
            print(profile_form.cleaned_data)
            return redirect('add_profiles')
    
    else:
        profile_form = forms.Add_profile()
    return render(res, 'add_profile.html', {'form' : profile_form})
