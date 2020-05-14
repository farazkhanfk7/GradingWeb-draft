from django import forms
from .models import Mark,Student,Math,Physics,Chem,Test,Simple

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['marks_obtain','upload']

class MathForm(forms.ModelForm):
    class Meta:
        model = Math
        fields = ['marks_obtain','upload']

class PhyForm(forms.ModelForm):
    class Meta:
        model = Physics
        fields = ['marks_obtain','upload']

class ChemForm(forms.ModelForm):
    class Meta:
        model = Chem
        fields = ['subcode','marks_obtain','upload']

class StudForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('studname','studroll','coursename','branchname','sem','mobile','adhar','gen','add','city','state','country','dob','father','mother','religion','category','reg','year','session')

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('roll','name','upload')

class SimpForm(forms.ModelForm):
    class Meta:
        model = Simple
        fields = ['name','city']