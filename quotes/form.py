from django import forms
from quotes.models import Quote,Individual

class CreateForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'