from django.urls import path, re_path

from . import views

urlpatterns = (
    path(r'login/', views.Login.as_view(), name="API Login"),
    re_path(r'^logout/', views.Logout.as_view(), name="API Logout"),
    re_path(r'^refresh-token/(?P<token>\w+)/$', views.RefreshToken.as_view(), name="Refresh Token"),
    
    path(r'current-user/', views.CurrentUserContext.as_view(), name="Current User"),

    re_path(r'^forgot-password/(?P<username>\w+)/$', views.ForgotPassword.as_view(), name="Forgot Password"),
    re_path(r'^validate-forgot-password-reset-token/(?P<token>\w+)/$', views.ValidateForgotPasswordResetToken.as_view(), name="Validate Forgot Password Reset Token"),
    re_path(r'^forgot-password-reset/(?P<token>\w+)/$', views.ForgotPasswordReset.as_view(), name="Forgot Password Reset"),
)
