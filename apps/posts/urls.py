from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail_url'),
    path('post/create', views.post_create, name='post_create')
]
