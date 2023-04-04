from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('', views.login_user, name='login_user'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/maintenance/new', views.dashboard_maintenance_new, name='dashboard_maintenance_new'),
    path('dashboard/maintenance/<id>/edit', views.dashboard_maintenance_edit, name='dashboard_maintenance_edit'),
]
