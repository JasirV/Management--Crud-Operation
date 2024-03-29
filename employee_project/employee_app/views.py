from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employe
# Create your views here.
def employee_list(request):
    context={'employee_list':Employe.objects.all()}
    return render(request,'employee_app/employee_list.html',context)
def employee_form(request,id=0):
    if request.method=='GET':
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employe.objects.get(pk=id)
            form = EmployeeForm(instance=employee)

        return render(request,'employee_app/employee_form.html',{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employe.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list/')
    
def employee_delete(request,id):
    employee = Employe.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list/')