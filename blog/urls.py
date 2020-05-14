from django.urls import path
from django.conf import settings # importing settings because we'll use variables defined there
from . import views

app_name= 'blog'
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
