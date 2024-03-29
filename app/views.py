from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags

from app.models import Maintenance


@login_required(login_url='users:login_user', redirect_field_name='next')
def home(request):
    data = Maintenance.objects.filter(is_finished=True, owner=request.user).order_by('-id')
    return render(request, 'templates/app/pages/home.html', context={'contents': data})


@login_required(login_url='users:login_user', redirect_field_name='next')
def content(request, id):
    data = get_object_or_404(Maintenance, pk=id, is_finished=True)
    return render(request, 'templates/app/pages/content_view.html', context={'content': data, 'is_detail_view': True})


def send_email(request, id):
    data = get_object_or_404(Maintenance, pk=id, is_finished=True)

    mail_title = 'Maintenance'
    html_content = render_to_string('templates/app/emails/next_maintenance.html', context={
        'request': request,
        'data': data,
    })
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(mail_title, text_content, settings.EMAIL_HOST_USER, [data.owner.email])
    email.attach_alternative(html_content, 'text/html')
    email.send()

    return redirect(reverse('users:dashboard'))
    # return render(request, 'templates/app/emails/sent_email.html')
