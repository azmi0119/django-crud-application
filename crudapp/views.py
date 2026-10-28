from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import DepartmentForm, EmployeeForm
from .models import Department, Employee
def employee_list(request): return render(request,"crudapp/employee_list.html",{"employees":Employee.objects.select_related("department").all()})
def employee_create(request):
    form=EmployeeForm(request.POST or None,request.FILES or None)
    if request.method=="POST" and form.is_valid():
        employee=form.save()
        try:
            if settings.EMAIL_HOST_USER and settings.EMAIL_HOST_PASSWORD:
                send_mail(f"New employee created: {employee.name}",f"Employee created\nName: {employee.name}\nAge: {employee.age}\nDepartment: {employee.department.name}\nGender: {employee.gender}\nHobbies: {', '.join(employee.hobbies) or 'None'}\nEmail: {employee.email}",settings.DEFAULT_FROM_EMAIL,[employee.email],fail_silently=False)
                messages.success(request,"Employee created. Notification email sent to the employee's email address.")
            else: messages.warning(request,"Employee created, but Mailtrap credentials are not configured in .env.")
        except Exception: messages.warning(request,"Employee created, but email failed. Check Mailtrap settings.")
        return redirect("employee_list")
    return render(request,"crudapp/employee_form.html",{"form":form,"page_title":"Add Employee","button_text":"Create Employee"})
def employee_update(request,pk):
    employee=get_object_or_404(Employee,pk=pk); form=EmployeeForm(request.POST or None,request.FILES or None,instance=employee)
    if request.method=="POST" and form.is_valid(): form.save(); messages.success(request,"Employee updated."); return redirect("employee_list")
    return render(request,"crudapp/employee_form.html",{"form":form,"page_title":"Edit Employee","button_text":"Save Changes","employee":employee})
def employee_delete(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    if request.method=="POST": employee.delete(); messages.success(request,"Employee deleted."); return redirect("employee_list")
    return render(request,"crudapp/confirm_delete.html",{"object":employee,"cancel_url":reverse("employee_list"),"object_type":"employee"})
def department_list(request): return render(request,"crudapp/department_list.html",{"departments":Department.objects.all()})
def department_create(request):
    form=DepartmentForm(request.POST or None)
    if request.method=="POST" and form.is_valid(): form.save(); messages.success(request,"Department created."); return redirect("department_list")
    return render(request,"crudapp/department_form.html",{"form":form,"page_title":"Add Department"})
def department_update(request,pk):
    obj=get_object_or_404(Department,pk=pk); form=DepartmentForm(request.POST or None,instance=obj)
    if request.method=="POST" and form.is_valid(): form.save(); messages.success(request,"Department updated."); return redirect("department_list")
    return render(request,"crudapp/department_form.html",{"form":form,"page_title":"Edit Department"})
def department_delete(request,pk):
    obj=get_object_or_404(Department,pk=pk)
    if request.method=="POST":
        if obj.employees.exists(): messages.error(request,"This department has employees. Reassign or delete them first.")
        else: obj.delete(); messages.success(request,"Department deleted.")
        return redirect("department_list")
    return render(request,"crudapp/confirm_delete.html",{"object":obj,"cancel_url":reverse("department_list"),"object_type":"department"})
