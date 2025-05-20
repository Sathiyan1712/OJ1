from django.urls import path
from . import views

urlpatterns=[
    path("",views.home, name='home'),
    path("chose-action",views.choose_action, name='chose it'),
    path("register-teacher", views.Register_teach, name='regis-teach'),
    path("register-student", views.Register_stud, name='regis-stud'),
    path("login-teacher", views.Login_teach, name='login-teach'),
    path("login-student", views.Login_stud, name='login-stud'),
]