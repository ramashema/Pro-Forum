from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def confirm_logout(request):
    """This is the view function for confirming log out"""
    return render(request, 'registration/confirm_logout.html')


def register(request):
    """This is the view function for user resgistration"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user) # give the new user the session

            return redirect('posts:home')

    context = {'form': form}
    return render(request, 'registration/register.html', context)