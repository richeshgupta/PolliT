from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import SignUpForm
# Create your views here.
def home(request):
    return render(request,"users/index.html",{})

def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # form = form.cleaned_data()
            form.save()
    else:
        form = SignUpForm()

    return render(request,"users/signup.html",{'form':form})
