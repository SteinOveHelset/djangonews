from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
