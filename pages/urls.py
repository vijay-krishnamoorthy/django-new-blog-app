from django.urls import path, include
from pages import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('posts/',views.PostList.as_view(),name='Home'),
    path('posts/<slug:slug>/',views.PostDetail.as_view(), name='post_detail'),
]