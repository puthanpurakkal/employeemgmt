from django.urls import path
from employee import views
urlpatterns = [

 # path("index",views.LoginView.as_view()),
 #     path("register",views.RegistrationView.as_view()),
 #     path("profile/add",views.EmployeeCreateView.as_view(),name="emp-add")
 path("",views.index, name="index"),
 path("add", views.EmployeeCreateView.as_view(), name="emp-create"),
 path("all", views.EmployeeListView.as_view(), name="emp-list"),
 path("details/<str:emp_id>", views.EmployeeDetailView.as_view(), name="emp-detail"),
 path("change/<str:e_id>", views.EmployeeEditView.as_view(), name="emp-edit"),
 path("remove/<str:e_id>",views.EmployeeDeleteView.as_view(), name="emp-remove"),
 path("accounts/signin",views.SignUpView.as_view(), name="signup")
]
