from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        #if user has detail and want an account
        if request.POST['psw1'] == request.POST['psw2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html',{'error':'Username taken, try another !'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['psw1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password must match!'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect.'} )
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    # to do need to route homepage
    ##and don't forget to logout
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')