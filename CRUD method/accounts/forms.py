from .models import Testmodel
from django import forms

class BannerForm(forms.ModelForm):
    class Meta:
        model = Testmodel #Or Banner ??
        fields = ('name','file')