from django.shortcuts import render, redirect
from first_app.forms import RegistrationForm, change_user_data
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
# Create your views here.
def home(request):
    return render(request, './home.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Signup Successful')
            form.save(commit=True)
            print (form.cleaned_data)
            return redirect('user_login')
    else:
        form = RegistrationForm()
    return render(request, './signup.html', {'form': form})


def user_login(request):  
    if request.method == 'POST':
        form = AuthenticationForm(request.user, data=request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            
            user = authenticate(username = name, password = user_pass)
            
            if user is not None:
                messages.success(request, 'Logged In Successfully')
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, './user_login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.warning(request, 'Logged out Successfully')
    return redirect('user_login')
    
def profile(request):
    return render(request, './profile.html')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, data = request.POST)
            if form.is_valid():
                form.save(commit=True)
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully using old password') 
                return redirect('profile')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, './pass_change.html', {'form': form})
    else:
        return redirect('user_login')
    
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.user, data = request.POST)
            if form.is_valid():
                form.save(commit=True)
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully without using old password') 
                return redirect('profile')
        else:
            form = SetPasswordForm(request.user)
        return render(request, './pass_change.html', {'form': form})
    else:
        return redirect('user_login')

def change_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = change_user_data(request.POST, instance = request.user)
            if form.is_valid():
                form.save(commit=True)
                messages.success(request, 'User data changed successfully') 
                return redirect('profile')
        else:
            form = change_user_data(instance=request.user)
        return render(request, './change_data.html', {'form': form})
    else:
        return redirect('user_login')