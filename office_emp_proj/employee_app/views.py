from http.client import HTTPResponse
from django.shortcuts import render
from datetime import datetime
from .models import Employee
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    param={'emps':emps}
    return render(request,'all_emp.html',param)


def add_emp(request):
    return render(request,'add_emp.html')

def add(request):
    if request.method == 'POST':
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        emailid=request.POST.get("email")
        dept=(request.POST.get("dept"))
        salary=int(request.POST.get("salary"))
        bonus=int(request.POST.get("bonus"))
        role=int(request.POST.get("role"))
        phone=request.POST.get("phone")
        date=request.POST.get("hdate")
        myemp= Employee(first_name = fname,last_name =lname,email = emailid, dept_id=dept, salary=salary, bonus=bonus, role_id=role, phone=phone, hire_date=datetime.now())
        myemp.save()
        param={'msg':'Record Added Successfully'}
        return render(request,"add_emp.html",param)
    else:
        param={'msg':'OOPs You Are Unable To Add Record Try Again Plaese'}
        return render(request,"add_emp.html",param)


def rem_emp(request):
    emps=Employee.objects.all()
    param={"emp":emps}
    return render(request,'rem_emp.html',param)

def remove(request,emp_id=0):
    if emp_id:
        try:
            emp=Employee.objects.filter(id=emp_id)
            emp.delete()
            param={"msg":"Employee Removed Successfully!!"}
            return render(request,"rem_emp.html",param)
        except:
            return HTTPResponse("Please Enter A Valid Employee Id")
    else:
        return HTTPResponse("Oops Something Went Wrong")


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('empname')
        dept = request.POST.get('deptname')
        role = request.POST.get('emprole')
        emps=Employee.objects.all()
        if name:
            emps = Employee.objects.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = Employee.objects.filter(Q(dept__name__icontains = dept))
        if role:
            emps = Employee.objects.filter(Q(role__name__icontains = role))
        param={'emps':emps}
        return render(request,'all_emp.html',param)
    else:
        return render(request,'filter_emp.html')


def dept(request):
    return render(request,'dept.html')

def role(request):
    return render(request,'role.html')