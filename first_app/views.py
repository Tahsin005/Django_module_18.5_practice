from django.shortcuts import render, redirect
from first_app.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
# Create your views here.
def home(request):
    return render(request, './home.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print (form.cleaned_data)
            messages.success(request, 'Signup Successful')
            return redirect('home')
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
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, './user_login.html', {'form': form})