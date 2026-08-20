from django import forms
from .models import UserProfile

class UserUpdateProfile(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['photo','notes']

