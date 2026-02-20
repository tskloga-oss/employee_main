from  django.http import HttpResponse
from employee.models import Employee
from django.shortcuts import render

def home(request):
    # Fetch the data from Employee table and display  in the console
    emp = Employee.objects.all()
    print(emp)
    # return HttpResponse(emp)  #output -> Architha GaneshamoorthyJohn Doe
    
    # emp_names = ", ".join([str(e) for e in emp])  # uses __str__ from your Employee model
    # return HttpResponse(f"<h1>{emp_names}</h1>")  # output -> <h1>Architha Ganeshamoorthy, John Doe</h1>

    # Render the data in a template
    context = {
        'employees': emp
    }
    return render(request, 'home.html', context=context)