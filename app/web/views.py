from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def home(request):
    return render(request, 'app/pages/home.html')


def send_email(request):
    html_content = render_to_string(
        'app/emails/next_maintenance.html',
        context={
            'name': 'Felipe',
            'next_date': '2022-12-25',
        }
    )
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        'Maintenance', text_content, settings.EMAIL_HOST_USER,
        ['felipetreis1@gmail.com']
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()

    return HttpResponse('sent email')
