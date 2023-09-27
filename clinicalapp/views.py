from django.shortcuts import render,redirect
from clinicalapp.models import patient,clinicaldata
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from clinicalapp.forms import clinicaldataform
# Create your views here.
class patientListView(ListView):
    model=patient

class patientcreateview(CreateView):
    model=patient
    fields=('firstname','lastname','age')
    success_url = reverse_lazy('index')

class patientupdateview(UpdateView):
    model=patient
    # reverse_url=reverse_lazy('index')
    fields=('firstname','lastname','age')
    success_url=reverse_lazy('index')

class patientdeleteview(DeleteView):
    model=patient
    success_url=reverse_lazy('index')

def adddata(request,**kwargs):
    form=clinicaldataform()
    patients= patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=clinicaldataform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalapp/clinicaldata_form.html',{'form':form,'patient':patients})


def analyze(request,**kwargs):
    data=clinicaldata.objects.filter(patients_id=kwargs['pk'])
    responsedata=[]
    for each in data:
        if each.componentname=='hw':
            handw=each.componentvalue.split('/')
            if len(handw)>1:
                feettomtrs=float(handw[0])*0.4536
                BMI=(float(handw[1])/feettomtrs*feettomtrs)
                bmientry=clinicaldata()
                bmientry.componentname='BMI'
                bmientry.componentvalue=BMI
                responsedata.append(bmientry)
        responsedata.append(each)
    return render(request,'clinicalapp/generatereport.html',{'data':responsedata})