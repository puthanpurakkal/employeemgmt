from django.urls import path
from employee import views
urlpatterns = [

 # path("index",views.LoginView.as_view()),
 #     path("register",views.RegistrationView.as_view()),
 #     path("profile/add",views.EmployeeCreateView.as_view(),name="emp-add")

 path("add", views.EmployeeCreateView.as_view(), name="emp-create")

 ]
