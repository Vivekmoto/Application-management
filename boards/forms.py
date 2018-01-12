from boards.models import Complaints
from django import forms
from django.forms import ModelForm

class ComplaintForm(ModelForm):
    class Meta:
        model=Complaints
        fields=['ComplaintRegarding','ProblemFacedOn','ContactNo','DescribeYourIssue']
        db_table='Complaints'


