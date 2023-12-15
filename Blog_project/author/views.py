from django.shortcuts import render, redirect

from . import forms
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from posts.models import Post

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm


def RegisterForm(request):
    if request.method == "POST":
        form = forms.Register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Create SuccesssFully ")
            return redirect("Register")
    else:
        form = forms.Register()
    return render(request, "register.html", {"form": form, 'type': 'Register'})



def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data["username"]
            userpass = form.cleaned_data["password"]
            user = authenticate(username=name, password=userpass)
            if user is not None:
                messages.success(request, "Logged in Successfully ")
                login(request, user)
                return redirect("homePage")
            else:
                messages.warning(request,'Logged in Incorrent ')
                return redirect('Register')
    else:
        form = AuthenticationForm()
    return render(request, "register.html", {"form": form, 'type': 'login'})



def user_logout(request):
    logout(request)
    return redirect('login')


@ login_required
def profile(request):
    data = Post.objects.filter( Author=request.user)
    return render(request, 'profile.html',{'data':data})


@ login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance=request.user) 
    return render(request, 'update_profile.html', {'form': profile_form, 'type': 'Update Profile'})

def user_pass_change(requset):
    if requset.user.is_authenticated:
        if requset.method == 'POST':
            change_pass = PasswordChangeForm(requset.user, data = requset.POST)
            if change_pass.is_valid():
                change_pass.save()
                messages.success(requset,'Password Change Successfully')
                update_session_auth_hash(requset,change_pass.user)
                return redirect('profile')
        else:
            change_pass = PasswordChangeForm(user = requset.user)
        return render(requset,'ChangePass.html',{'form':change_pass ,'type':'Password Change'})
    else:
        return redirect('login')
