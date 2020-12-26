from django.shortcuts import render, HttpResponseRedirect
from .models import DOCTOR_DETAILS,DOCTOR_MONITOR as dm
from nurse.models import NURSE_DETAILS,NURSE_MONITOR as nm
from ward.models import NURSE_WORKS as nw, DOCTOR_WORKS as dw, WARD_MANAGED_BY as wm

# Create your views here.
def DetailChoices(request):
    if request.method == 'POST':
        choice = str(request.POST.get('ddchoice'))
        if choice=='Get all Doctor Details':
            doctors= DOCTOR_DETAILS.objects.all()
            return render(request,'Doctor/index.html',{'doctors' : doctors})
        elif choice=='Individual Doctor Details':
            return HttpResponseRedirect('single-doctor-details/')
        elif choice==' Get all Nurse Details ':
            nurses= NURSE_DETAILS.objects.all()
            return render(request,'Doctor/index.html',{'nurses' : nurses})
        elif choice=='Individual Nurse Details':
            return HttpResponseRedirect('single-nurse-details/')

        else:
            return render(request, 'Doctor/index.html')    
    else: 
        return render(request,'Doctor/index.html',{'home':'/'})

def DoctorDetails(request):
    if request.method=="POST":
        id=request.POST.get('Did')
        dmonitor,wards = [],[]
        try:
            doctor = DOCTOR_DETAILS.objects.get(Dr_id=id)
 
            if dm.objects.filter(Drid=id).exists():
                dmonitor= dm.objects.filter(Drid=id)[:5]
            
            if dw.objects.filter(Doc_ID=id).exists():
                wards= dw.objects.filter(Doc_ID=id)
            return render(request,'Doctor/doctordetails.html',{'doctor' : [doctor],'dmonitor':dmonitor,'wards':wards})
        except Exception as e:
            print(e)
            return render(request,'Doctor/doctordetails.html',{'doctor': [],'error':e})
    else:
        return render(request, 'Doctor/doctordetails.html',{'link':'/doctor-and-nurse/'})

def NurseDetails(request):
    if request.method=="POST":
        id=request.POST.get('Nid')
        nmonitor,wards,mngward = [],[],[]
        try:
            nurse = NURSE_DETAILS.objects.get(Nurse_id=id)
            if nm.objects.filter(Nid=id).exists():
                nmonitor= nm.objects.filter(Nid=id)[:5]
            if nw.objects.filter(Nurse_ID=id).exists():
                wards= nw.objects.filter(Nurse_ID=id)
            if wm.objects.filter(MgrNurse_ID=id).exists():
                mngward= wm.objects.filter(MgrNurse_ID=id)

            return render(request,'Doctor/nursedetails.html',{'nurse' : [nurse],'nmonitor':nmonitor,'wards':wards,'mngward':mngward})
        except Exception as e:
            print(e)
            return render(request,'Doctor/nursedetails.html',{'nurse': [],'error':e})
    else:
        return render(request, 'Doctor/nursedetails.html',{'link':'/doctor-and-nurse/'})