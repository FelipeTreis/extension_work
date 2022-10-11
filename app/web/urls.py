from app.web import views
from django.urls import path

app_name = 'web'

urlpatterns = [
    path('', views.home, name='home'),
    path('send-email/', views.send_email, name='send_email')
]
