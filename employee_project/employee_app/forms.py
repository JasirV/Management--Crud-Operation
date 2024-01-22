from django import forms
from .models import Employe

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ('fullname','emp_code','mobile','position')
        labels={'fullname':'Full Name','emp_code':'Employees Id','mobile':'Mobile','position':'Position'}
    def __init__(self,*args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label='Select'
        self.fields['emp_code'].required=False