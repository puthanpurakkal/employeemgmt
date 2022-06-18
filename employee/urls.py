from django.urls import path
from employee import views
urlpatterns = [

 # path("index",views.LoginView.as_view()),
 #     path("register",views.RegistrationView.as_view()),
 #     path("profile/add",views.EmployeeCreateView.as_view(),name="emp-add")

 path("add", views.EmployeeCreateView.as_view(), name="emp-create"),
 path("all", views.EmployeeListView.as_view(), name="emp-list"),
 path("details/<str:emp_id>", views.EmployeeDetailView.as_view(), name="emp-detail")

 ]
