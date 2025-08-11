from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignupForm
from .models import Users


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            Users.objects.create(user=user)

            return redirect('/log-in/')
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', { 
        'form' : form
    })

@login_required
def myaccount(request):       
    return render(request, 'users/myaccount.html')