from django import forms
#
# class EmployeeForm(forms.Form):
#     eid = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     employee_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     designation = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     Salary = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     Email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
#     experience = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     def clean(self):
#         cleaned_data=super().clean()
#         exp=cleaned_data.get("experience")
#         sal=cleaned_data.get("Salary")
#         if exp<0:
#             msg="Invalid Experience"
#             self.add_error("experience",msg)
#         if sal<0:
#             msg1 = "Invalid Salary"
#             self.add_error("Salary", msg1)
#

class EmployeeCreateForm(forms.Form):
    eid = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    employee_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    designation= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    salary= forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    experience=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))