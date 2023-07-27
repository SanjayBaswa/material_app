from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
# Create your views here.


def HomeRecords(request):

    query_set = Datatable.objects.all()

    context = {
        'query_set' : query_set
    }
    print(context)
    return render(request , 'record_table.html' , context) 
    

def SaveData(request):
    if request.method == 'POST':
       Date =  request.POST["Date"]
       ItemName  = request.POST["ItemName"]
       Customer  = request.POST["Customer"]
       Project  = request.POST["Project"]
       DCNumber  = request.POST["DCNumber"]
       PartNumber  = request.POST["PartNumber"]
       Returnable = request.POST["Returnable"]
       Remarks  = request.POST["Remarks"]

       Datatable.objects.create(
             item=ItemName, customer=Customer, dc_no=DCNumber, Part_no=PartNumber, returnable=Returnable, remarks=Remarks, project=Project, 
            date=Date, time_stamp=datetime.datetime.now())
    return redirect("/records/")
    
def material_form(request):
    return render(request, "forms copy.html" )
    
def delete(request , id):
    print(id)
    record_to_delete = Datatable.objects.get(id=id)
    # Delete the record
    record_to_delete.delete()
    return redirect("/records/")

