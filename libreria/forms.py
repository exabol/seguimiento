from django import forms
from .models import Ilcs

class IlcForm(forms.ModelForm):
    class Meta:
        model = Ilcs
        fields = '__all__'