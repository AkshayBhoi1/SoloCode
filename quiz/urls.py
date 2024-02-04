from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('lg/', views.loginpage, name='loginpage'),
    path('sign/', views.signup, name='signuppage'),
    path('index/', views.index, name='index'),
    path('c/', views.c, name='c'),
    path('cpp/', views.cpp, name='cpp'),
    path('python/', views.python, name='python'),
    path('java/', views.java, name='java'),
    path('js/', views.js, name='js'),
    path('php/', views.php, name='php'),
    path('', views.home, name='home'),
    path('gen_cer/', views.gen_cer, name='gen_cer'),
    path('logout/', views.logout_view, name='logout'),
    path('score/', views.score, name='score'),
    path('certificate/', views.certificate, name='certificate'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),


]


