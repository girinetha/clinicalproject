from django import forms
from clinicalapp.models import clinicaldata,patient

class patientform(forms.ModelForm):
    class Meta:
        model=patient
        fields='__all__'

class clinicaldataform(forms.ModelForm):
    class Meta:
        model=clinicaldata
        fields='__all__'
