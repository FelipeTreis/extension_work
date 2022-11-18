from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from app.models import Maintenance
from users.forms import LoginForm, MaintenanceForm, RegisterForm


def register(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'templates/app/pages/register.html', {'form': form, 'form_action': reverse('users:register_create'), })


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
    return render(request, 'templates/app/pages/login.html', {'form': form, 'form_action': reverse('users:login_create'), })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

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
    return redirect(reverse('users:dashboard'))


@login_required(login_url='users:login_user', redirect_field_name='next')
def logout_user(request):
    if not request.POST:
        return redirect(reverse('users:login_user'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('users:login_user'))

    logout(request)
    return redirect(reverse('users:login_user'))


@login_required(login_url='users:login_user', redirect_field_name='next')
def dashboard(request):
    data = Maintenance.objects.filter(is_finished=True, owner=request.user)
    return render(request, 'templates/app/pages/dashboard.html', {'data': data})


@login_required(login_url='users:login_user', redirect_field_name='next')
def dashboard_maintenance_new(request):
    form = MaintenanceForm(request.POST or None)

    if form.is_valid():
        data: Maintenance = form.save(commit=False)
        data.owner = request.user
        data.save()
        messages.success(request, 'Your maintenance has been successfully saved!')
        return redirect(reverse('users:dashboard'))

    return render(request, 'templates/app/pages/dashboard_maintenance.html',
                  {'form': form, 'form_action': reverse('users:dashboard_maintenance_new')}
                  )


@login_required(login_url='users:login_user', redirect_field_name='next')
def dashboard_maintenance_edit(request, id):
    data = Maintenance.objects.get(is_finished=True, owner=request.user, pk=id)
    form = MaintenanceForm(request.POST or None, instance=data)

    if form.is_valid():
        data.owner = request.user
        data.save()
        messages.success(request, 'Your maintenance has been successfully saved!')
        return redirect(reverse('users:dashboard'))

    return render(request, 'templates/app/pages/dashboard_maintenance.html', {'form': form, 'data': data})
