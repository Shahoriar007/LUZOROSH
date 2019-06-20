from django.urls import path,include
from .views import index,register
from django.contrib.auth.views import (
     LoginView, LogoutView,
)
app_name='user'
urlpatterns = [
    path('', index.as_view(),name="index"),
    path('signup/', register,name="register"),
     path('login/', LoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='user/logged_out.html'), name="logout"),
]
