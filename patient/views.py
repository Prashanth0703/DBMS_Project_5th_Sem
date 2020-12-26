from django.shortcuts import render,HttpResponseRedirect
from django.db import connection
from .models import PATIENT_DETAILS as b, ADMITTED_TO as a, PAYMENT as p, HAS_BANK as hb, HAS_INSURANCE as hi, DECISION_MAKING as dm, HOME_QUARANTINE_MONITOR as hqm, DEPENDENT as d
from django.contrib import messages

# Create your views here.
def PatientDetails(request):
    if request.method=="POST":
        id=request.POST.get('P_id')
        payment,bankdet,hqmd,insurance,diagnosis,dep,adm = [],[],[],[],[],[],[]
        try:
            patient = b.objects.get(P_id=request.POST.get('P_id'))
            if p.objects.filter(Patient_id=id).exists():
                payment= p.objects.filter(Patient_id=request.POST.get('P_id'))
            if dm.objects.filter(Pid=request.POST.get('P_id')).exists():
                diagnosis= dm.objects.filter(Pid=request.POST.get('P_id'))
            if hqm.objects.filter(Pat_ID=request.POST.get('P_id')).exists():
                hqmd= hqm.objects.filter(Pat_ID=request.POST.get('P_id'))
            if a.objects.filter(Pat_ID=request.POST.get('P_id')).exists():
                adm= a.objects.filter(Pat_ID=request.POST.get('P_id'))

            if d.objects.filter(Patient_id=id).exists():
                dep=d.objects.filter(Patient_id=id)
            if hb.objects.filter(Patient_id=request.POST.get('P_id')).exists():
                bankdet= hb.objects.filter(Patient_id=request.POST.get('P_id'))
            if hi.objects.filter(Patient_id=request.POST.get('P_id')).exists():
                insurance= hi.objects.filter(Patient_id=request.POST.get('P_id'))

            return render(request,'Patient/patientdetails.html',{'patient' : [patient],'payment':payment,'adm':adm, 'bankdetails':bankdet,'insurance':insurance,'diagnosis':diagnosis,'hqmd':hqmd,'dep':dep,'link':'/patient/'})
        except Exception as e:
            print(e)
            messages.error(request,"Enter valid Patinet ID")
            return render(request,'Patient/patientdetails.html',{'patient': [],'error':e})
    else:
        return render(request, 'Patient/patientdetails.html',{'link':'/patient/'})

def DetailChoices(request):
    if request.method == 'POST':
        choice = str(request.POST.get('pdchoice'))
        if choice=='Get patient details':
            patients= b.objects.all()
            return render(request,'Patient/index.html',{'patients' : patients})
        elif choice=='Admitted Patient Details':
            cursor = connection.cursor()
            cursor.execute('select b.P_id,b.name,b.Age,b.Gender,b.City,b.Street,b.Pincode,b.Symptomatic,b.Previous_Disease,b.Still_Exists,a.Ward_ID_id,a.Priority,a.Health_Score from PATIENT_DETAILS as b join ADMITTED_TO as a on b.P_id=a.Pat_ID_id')
            result=cursor.fetchall()
            return render(request,'Patient/index.html',{'adpat' : result})
        elif choice=='HomeQuarantine Patient Details':
            cursor = connection.cursor()
            cursor.execute('select b.P_id,b.name,b.Age,b.Gender,b.City,b.Street,b.Pincode,b.Symptomatic,b.Previous_Disease,b.Still_Exists,a.Health_Status,a.Movements from PATIENT_DETAILS as b join HOME_QUARANTINE_MONITOR as a on b.P_id=a.Pat_ID_id')
            result=cursor.fetchall()
            return render(request,'Patient/index.html',{'hqpat' : result})
        elif choice=='Individual Patient Details':
            return HttpResponseRedirect('single-patient-details/')

        else:    
            return render(request, 'Patient/index.html',{'home':'/'})    
    else: 
        return render(request,'Patient/index.html',{'home':'/'})

