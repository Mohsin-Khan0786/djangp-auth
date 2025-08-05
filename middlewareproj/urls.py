from django.urls import path
from .views import (
    HomeView, LoginPageView, LogoutPageView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login-page/', LoginPageView.as_view(), name='login_page'),
    path('logout-page/', LogoutPageView.as_view(), name='logout_page'),
]