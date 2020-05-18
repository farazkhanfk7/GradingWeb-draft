from django import forms
from .models import Student,Test,Simple,Subject,Marks


class SubForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['Subject_Name','Subject_Code','Max_Marks','Course','Branch','Semester']

class MarkForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['subcode','marks','sheet']
        widgets = {
            'subcode':forms.Select(attrs={'class':'form-control'}),
            'marks':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Marks'}),
            'sheet':forms.FileInput(attrs={'class':'form-control'})
        }

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