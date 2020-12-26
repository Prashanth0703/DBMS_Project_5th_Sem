from django.shortcuts import render,HttpResponseRedirect
from django.db import connection
from .models import WARD_DETAILS, DOCTOR_WORKS as dw,WARD_MANAGED_BY as wm, NURSE_WORKS as nw
from patient.models import ADMITTED_TO as aw

# Create your views here.
def DetailChoices(request):
    if request.method == 'POST':
        choice = str(request.POST.get('wdchoice'))
        if choice=='Get all ward details':
            wards= WARD_DETAILS.objects.all()
            return render(request,'Ward/index.html',{'wards' : wards})
        elif choice=='Individual Ward Details':
            return HttpResponseRedirect('single-ward-details/')
       
        else:
            return render(request, 'Ward/index.html')    
    else: 
        return render(request,'Ward/index.html',{'home':'/'})

def WardDetails(request):
    if request.method=="POST":
        id=request.POST.get('Wid')
        doctors,nurses,patients,manager = [],[],[],[]
        try:
            ward = WARD_DETAILS.objects.get(Ward_No=id)
 
            if dw.objects.filter(Ward_ID=id).exists():
                doctors= dw.objects.filter(Ward_ID=id)
            if nw.objects.filter(Ward_ID=id).exists():
                nurses= nw.objects.filter(Ward_ID=id)
            if aw.objects.filter(Ward_ID=id).exists():
                patients= aw.objects.filter(Ward_ID=id)
            if wm.objects.filter(Ward_ID=id).exists():
                manager= wm.objects.filter(Ward_ID=id)

            return render(request,'Ward/warddetails.html',{'ward' : [ward],'doctors':doctors,'nurses':nurses,'patients':patients,'manager':manager})
        except Exception as e:
            print(e)
            return render(request,'Ward/warddetails.html',{'ward': [],'error':e})
    else:
        return render(request, 'Ward/warddetails.html',{'link':'/ward/'})