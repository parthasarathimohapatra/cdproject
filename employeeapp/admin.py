from django.contrib import admin
from employeeapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','ecity','start_time','end_time']
admin.site.register(Employee,EmployeeAdmin)
