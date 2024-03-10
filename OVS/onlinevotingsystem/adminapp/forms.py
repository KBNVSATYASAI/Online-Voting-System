from django import forms
from django.contrib.auth.backends import ModelBackend
from django_otp.views import login

from .models import Voter


class VoterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.TextInput())  # Change to TextInput for visibility

    class Meta:
        model = Voter
        fields = ['username', 'epic_number', 'password']
