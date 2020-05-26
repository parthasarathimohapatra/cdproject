from django.shortcuts import render,redirect
from employeeapp.models import Employee
from employeeapp.forms import EmployeeForm

# Create your views here.
def retrieve_view(request):
    employee=Employee.objects.all()
    return render(request,'application/index.html',{'employee':employee})

def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'employeeapp/create.html',{'form':form})

def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'employeeapp/update.html',{'emp':emp})



# Create your views here.
