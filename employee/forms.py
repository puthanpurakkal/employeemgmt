from django import forms

class EmployeeForm(forms.Form):
    eid=forms.CharField()
    employee_name=forms.CharField()
    designation=forms.CharField()
    salary=forms.IntegerField()
    email=forms.EmailField()
    experience=forms.IntegerField()
