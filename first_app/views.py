from django.shortcuts import render, redirect
from first_app.forms import RegistrationForm
from django.contrib import messages
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


            