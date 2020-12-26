from django.shortcuts import render, HttpResponseRedirect

def HomePage(request):
    if request.method == 'POST':
        choice = str(request.POST.get('choice'))
        if choice=='Patient':
            return HttpResponseRedirect('patient/')    
        elif choice=='Doctor and Nurse':
            return HttpResponseRedirect('doctor-and-nurse/')   
        elif choice=='Ward':
            return HttpResponseRedirect('ward/')   
    else:
        return render(request, 'Hospital/home.html')