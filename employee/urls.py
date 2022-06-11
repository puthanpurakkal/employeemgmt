from django.urls import path
from employee import views
urlpatterns=[
#     path('index',views.index),
#     path('login',views.login),
#     path('signup',views.registration)
path("index",views.LoginView.as_view()),
    path("register",views.RegistrationView.as_view())


 ]
