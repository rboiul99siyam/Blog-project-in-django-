from django import forms
from profiles.models import Profile
class Add_profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'