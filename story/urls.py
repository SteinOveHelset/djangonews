from django.urls import path

from . import views

app_name = 'story'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/vote/', views.vote, name='vote'),
    path('<int:pk>/unvote/', views.unvote, name='unvote'),
]
