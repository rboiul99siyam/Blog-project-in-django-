from django import forms

from catagories.models import Catagory

class CatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = '__all__'
        
        