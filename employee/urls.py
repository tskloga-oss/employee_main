from django.urls import path

from .views import employee_detail, add_employee,edit_employee

urlpatterns =[
    path('<int:id>/', employee_detail,name='employee_detail'),
    path('add/', add_employee,name='add_employee'),
    path('<int:id>/edit/',edit_employee,name='edit_employee')

]