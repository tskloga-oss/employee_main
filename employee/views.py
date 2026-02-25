from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Employee
from .forms import EmployeeForm



# Create your views here.
# def home(request):
#     return render(request, 'home.html')

def employee_detail(request, id):
    # Logic to fetch employee details based on the provided id
    # For example, you might query the database for the employee with the given id
    # employee = Employee.objects.get(id=id)
    # name = employee.full_name()
    
    # # For now, we'll just return a placeholder response
    # # return render(request, 'employee_detail.html', {'employee_id': id})
    # return HttpResponse(f"Hi {name}, <br> Please find your employee details below <br> Employee  ID: {id} <br> Department: {employee.department } <br> Position: {employee.designation}")

    print(request,id)
    employee = get_object_or_404(Employee, id=id)
    
    print(employee.full_name())
    context = {
        'emp': employee
 
    }

    return render(request,'employee/employee_detail.html', context=context)


def add_employee(request):

    if request.method == 'POST':
         print(request.POST)
         form = EmployeeForm(request.POST, request.FILES)
         if form.is_valid():
            form.save()
            return HttpResponse("Employee added successfully!")
         else:
             print(form.errors)
             return HttpResponse("Form is not valid. Please check the input data.")
         
    form = EmployeeForm()     
    context =  {
        'form': form,
        'message': 'This is the add employee page.'
    }

    return render(request, 'employee/add_employee.html', context=context)

def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponse("Employee updated successfully!")
        else:
            print(form.errors)
            return HttpResponse("Form is not valid. Please check the input data.")
    
    form = EmployeeForm(instance=employee)
    context = {
        'form': form,
        'message': 'This is the edit employee page.',
        'e': employee
    }

    return render(request, 'employee/edit_employee.html', context=context)