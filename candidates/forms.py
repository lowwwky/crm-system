from django import forms

from .models import HireCard

class CandidateUpdateForm(forms.ModelForm):

    class Meta:
        model = HireCard
        fields = ['resume_link','interview_date', 'status']
        ordering = ['interview_date','status']