from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import LoginForm, RegisterForm


def register(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'app/pages/register.html', {'form': form, 'form_action': reverse('users:register_create'), })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Your user has been created, please log in.')
        del (request.session['register_form_data'])
        return redirect(reverse('users:login_user'))

    return redirect('users:register')


def login_user(request):
    form = LoginForm()
    return render(request, 'app/pages/login.html', {'form': form, 'form_action': reverse('users:login_create'), })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('users:login_user')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )
        if authenticated_user is not None:
            messages.success(request, 'You are logged in')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid username or password')
    return redirect(login_url)


@login_required(login_url='users:login_user', redirect_field_name='next')
def logout_user(request):
    if not request.POST:
        return redirect(reverse('users:login_user'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('users:login_user'))

    logout(request)
    return redirect(reverse('users:login_user'))