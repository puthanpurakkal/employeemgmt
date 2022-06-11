
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


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