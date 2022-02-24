from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("ajaxlogin/", views.ajax_login, name="ajaxlogin"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout", views.log_out, name="logout"),
]
