from django import forms 
from .models import FUND_DETAILS 
#Forms here

class FUND_FORM(forms.ModelForm):
    
    class Meta:
        model =  FUND_DETAILS
        fields = ['fn','sn', 'tn','fu','su','tu']
    
