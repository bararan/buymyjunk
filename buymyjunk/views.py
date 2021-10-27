from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from profiles.models import Profile

def login_view(req):
    form = AuthenticationForm()
    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                if req.GET.get('next'): # If redirecting to a specific page post-login. This is automatically added to the request if user tries to access a specific page (e.g. /reports) before logging in.
                    return redirect(req.GET.get('next'))
                return redirect('items:list')
            messages.add_message(req, messages.ERROR, "Something went wrong. Please try again.")
    context = {
        'form': form,
    }
    return render(req, 'auth/login.html', context=context)

def register_view(req):
    form = UserCreationForm()
    if req.method == 'POST':
        form = UserCreationForm(data=req.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(req, username=username, password=password)
            login(req, user)
            messages.add_message(req, messages.SUCCESS, f"Welcome onboard, {username}!\nYou can now start selling and buying.")
            profile = Profile.objects.get(user=user)
            return redirect(profile.get_absolute_url())
    context = {'form': form}
    return render (req, 'auth/register.html', context=context)

def logout_view(req):
    logout(req)
    return redirect('login')