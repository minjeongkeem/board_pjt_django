from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseBadRequest
from django.contrib.auth import get_user_model

User = get_user_model()

@require_http_methods(['GET', 'POST'])
def signup(request):
    # 이미 회원가입한 사용자라면 
    if request.user.is_authenticated:
        return HttpResponseBadRequest ('이미 로그인 하였습니다')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect ('board:board_index')

    else:
        form = CustomUserCreationForm()
    context = {'form':form, }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    # login 한 사용자라면,
    if request.user.is_authenticated:
        return HttpResponseBadRequest('이미 로그인 하였습니다.')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('board:board_index')
        else:
            form = AuthenticationForm()
        context = {'form':form, }
        return render(request, 'accounts/login.html', context)
            

def logout(request):
    auth_logout(request)
    return redirect('board:board_index')

@require_safe
def profile(request, username):
    me = request.user
    profile_user = get_object_or_404(User, username=username)
    context = {'profile_user':profile_user, }
    return render(request, 'accounts/profile.html', context)