from .models import Place, EvalPlace
from django import forms

class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place

        fields = (
            'name',
            'categories',
            'state',
            'city',
            'postal_code'
        )

class EvaluationForm(forms.ModelForm):

    class Meta:
        model = EvalPlace

        fields = (
            'score',
            'price',
            'comment'
        )
