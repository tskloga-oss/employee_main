from django.contrib import admin
from .models import Department, Employee

# Customizing the admin interface for Employee model
class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['id','full_name','email','designation','joining_date','is_active','department','report_to']
    list_filter =['report_to']
    search_fields = ["first_name","last_name","email"]
    list_editable = ['designation','is_active']
    list_display_links = ['full_name','email']
    # ordering = ["-id"] descending order of id
    ordering = ["id"]  # ascending order of id


# Register your models here.
admin.site.register(Department)
admin.site.register(Employee,EmployeeAdmin)
