# from django.shortcuts import render
# from django.views import View
# from employee.forms import EmployeeCreateForm
from django.views.generic import View

# from django.contrib import messages
# # Create your views here.
# # def index(request):
# #     return render(request,"home.html")
# #
def login(request):
    return render(request, "login.html")
#
# # def registration(request):
# #     return render(request,"reg.html")
#
# #
# class LoginView(View):
# #
#     def get(self, request):
#         return render(request, "login.html")
#
#
# class RegistrationView(View):
#     def get(self,request):
#         return render(request,"reg.html")
#
#     def post(self,request):
#         print(request.POST.get("f_name"))
#         print(request.POST.get("l_name"))
#         print(request.POST.get("e_mail"))
#         print(request.POST.get("u_name"))
#         print(request.POST.get("pwd"))
#         return render(request,"reg.html")
#
# class EmployeeCreateView(View):
#     form_class=EmployeeForm
#     template_name="emp-add.html"
#
#     def get(self,request):
#         form=self.form_class()
#         return render(request,self.template_name,{"form":form})
#
#     def post(self,request):
#         form=self.form_class(request.POST)
#         print("values in request.POST")
#         print(request.POST)
#         if form.is_valid():
#             print("cleaned_data")
#             print(form.cleaned_data)
#             print(form.cleaned_data.get("eid"))
#             print(form.cleaned_data.get("employee_name"))
#             print(form.cleaned_data.get("designation"))
#             messages.success(request,"profile hasbeen added")
#             return render(request,self.template_name,{"form":form})
#         else:
#             messages.error(request,"profile adding failed")
#             return render(request,self.template_name,{"form":form})
#
# class person:
#     def __init__(self,n1):
#         print("here")
# p=person(10)


from django.shortcuts import render,redirect
from employee.forms import EmployeeCreateForm, UserRegistrationForm, LoginForm
from django.views.generic import View, ListView, DetailView, CreateView
from employee.models import Employee
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

def signin_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            messages.error(request,"you must login")
            return render("signin")
    return wrapper

@method_decorator(signin_required,name="dispatch")
class EmployeeCreateView(View):

    def get(self, request, *args, **kwargs):
        form = EmployeeCreateForm()
        return render(request, "emp-add.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form= EmployeeCreateForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
              # print(form.cleaned_data)
            # Employee.objects.create(
            #     eid=form.cleaned_data.get("eid"),
            #     employee_name=form.cleaned_data.get("employee_name"),
            #     designation=form.cleaned_data.get("designation"),
            #     salary=form.cleaned_data.get("salary"),
            #     email=form.cleaned_data.get("email"),
            #     experience=form.cleaned_data.get("experience")
            # )
            messages.success(request, "employee has been added")
            return redirect("emp-create")
        else:
            messages.error(request, "employee added failed")
            return render(request, "emp-add.html", {"form": form})

@method_decorator(signin_required,name="dispatch")
class EmployeeListView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            qs = Employee.objects.all()
            return render(request, "emp-list.html", {"employees": qs})
        else:
            messages.error(request,"you must login first")
            return redirect("signin")

@method_decorator(signin_required,name="dispatch")
class EmployeeDetailView(View):
    def get(self,request, *args, **kwargs):
        # kwargs={emp_id:emp_100}
        qs=Employee.objects.get(eid=kwargs.get("emp_id"))
        return render(request, "emp-detail.html",{"employee":qs})

@method_decorator(signin_required,name="dispatch")
class EmployeeEditView(View):
    def get(self, request, *args, **kwargs):
        eid = kwargs.get("e_id")
        employee = Employee.objects.get(eid=eid)
        form=EmployeeCreateForm(instance=employee)
        return render(request, "emp-edit.html", {"form": form})

    def post(self, request, *args, **kwargs):
        eid = kwargs.get("e_id")
        employee = Employee.objects.get(eid=eid)
        form = EmployeeCreateForm(request.POST, instance=employee, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "employee edited successfully")
            return render(request, "emp-add.html", {"form": form})
        else:
            messages.error(request, "employee edited failed")
            return render(request, "emp-add.html", {"form": form})

@method_decorator(signin_required,name='dispatch')
class EmployeeDeleteView(View):
    def get(self, request, *args, **kwargs):
        eid = kwargs.get("e_id")
        employee = Employee.objects.get(eid=eid)
        employee.delete()
        messages.success(request, "employee deleted successfully")
        return redirect("emp-list")


@signin_required
def index(request):
    return render(request, "base.html")

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return render(request, "registration.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"account created successfully")
            return redirect("signup")
        else:
            messages.error(request,"account creation failed")
            return render(request, "registration.html", {"form": form})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(username=uname, password=pwd)
            if user:
                print("success")
                login(request,user)
                return redirect("emp-list")
            else:
                return render(request, "login.html", {"form": form})

@signin_required
def sign_out(request, *args, **kwargs):
    logout(request)
    return redirect("signin")
