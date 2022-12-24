from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from .views import Home,SignUp

urlpatterns = [
    path('signup/',SignUp.as_view(),name='signup'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('login/',LoginView.as_view(template_name='chat/login.html'),name='login'),
    path('',Home.as_view(),name='chat'),
]