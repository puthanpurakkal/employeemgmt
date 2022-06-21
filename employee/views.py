# from django.shortcuts import render
# from django.views import View
# from employee.forms import EmployeeCreateForm
# from django.views.generic import View
# from django.contrib import messages
# # Create your views here.
# # def index(request):
# #     return render(request,"home.html")
# #
# # def login(request):
# #     return render(request,"login.html")
# #
# # def registration(request):
# #     return render(request,"reg.html")
#
#
# class LoginView(View):
#
#     def get(self,request):
#         return render(request,"login.html")
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
from employee.forms import EmployeeCreateForm
from django.views.generic import View
from employee.models import Employee
from django.contrib import messages

class EmployeeCreateView(View):

    def get(self, request, *args, **kwargs):
        form = EmployeeCreateForm()
        return render(request, "emp-add.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form= EmployeeCreateForm(request.POST)
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


class EmployeeListView(View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        return render(request, "emp-list.html", {"employees": qs})

class EmployeeDetailView(View):
    def get(self,request, *args, **kwargs):
        # kwargs={emp_id:emp_100}
        qs=Employee.objects.get(eid=kwargs.get("emp_id"))
        return render(request, "emp-detail.html",{"employee":qs})

class EmployeeEditView(View):
    def get(self,request, *args, **kwargs):
        eid=kwargs.get("e_id")
        employee=Employee.objects.get(eid=eid)
        form=EmployeeCreateForm(instance=employee)
        return render(request,"emp-edit.html",{"form":form})

    def post(self,request, *args, **kwargs):
        eid=kwargs.get("e_id")
        employee=Employee.objects.get(eid=eid)
        form=EmployeeCreateForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "employee edited successfully")
            return redirect("emp-add")
        else:
            messages.error(request, "employee edited failed")
            return render(request, "emp-add.html", {"form": form})


class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("e_id")
        employee=Employee.objects.get(eid=eid)
        employee.delete()
        messages.success(request, "employee deleted successfully")
        return redirect("emp-list")




