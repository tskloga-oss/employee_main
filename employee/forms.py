from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = ['first_name', 'last_name', 'email', 'designation', 'image', 'joining_date', 'salary', 'is_active', 'department', 
                #   'report_to','created_at','updated_at']
        fields = '__all__'  # This will include all fields from the Employee model in the form
        # You can also specify widgets for better form rendering if needed
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'})
        }