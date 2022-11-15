from django.urls import path

from app.web import views

app_name = 'web'

urlpatterns = [
    path('', views.home, name='home'),
    path('maintenance/<int:id>/', views.content, name='content'),
    path('send-email/<int:id>/', views.send_email, name='send_email')
]
