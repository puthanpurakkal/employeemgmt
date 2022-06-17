
from django.shortcuts import render
from django.views import View
from employee.forms import EmployeeForm

# Create your views here.
# def index(request):
#     return render(request,"home.html")
#
# def login(request):
#     return render(request,"login.html")
#
# def registration(request):
#     return render(request,"reg.html")


class LoginView(View):

    def get(self,request):
        return render(request,"login.html")


class RegistrationView(View):
    def get(self,request):
        return render(request,"reg.html")

    def post(self,request):
        print(request.POST.get("f_name"))
        print(request.POST.get("l_name"))
        print(request.POST.get("e_mail"))
        print(request.POST.get("u_name"))
        print(request.POST.get("pwd"))
        return render(request,"reg.html")

class EmployeeCreateView(View):
    form_class=EmployeeForm
    template_name="emp-add.html"

    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{"form":form})

    def post(self,request):
        form=self.form_class(request.POST)
        print("values in request.POST")
        print(request.POST)
        if form.is_valid():
            print("cleaned_data")
            print(form.cleaned_data)
            print(form.cleaned_data.get("eid"))
            print(form.cleaned_data.get("employee_name"))
            print(form.cleaned_data.get("designation"))
            return render(request,self.template_name,{"form":form})
        else:
            return render(request,self.template_name,{"form":form})

class person:
    def __init__(self,n1):
        print("here")
p=person(10)
