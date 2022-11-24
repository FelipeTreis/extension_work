from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('maintenance/<int:id>/', views.content, name='content'),
]
