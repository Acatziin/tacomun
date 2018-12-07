from places.models import Profile
from django import forms

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = (
            'phone',
            'postal_code',
            'birthday'
        )