from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Form class for users to request a collaboration 
    """
    class Meta:
        model = CollaborateRequest
        fields = ['name', 'email', 'message']

    def save(self, commit=True):
        # ensure `read` stays False for new requests
        instance = super().save(commit=False)
        instance.read = False
        if commit:
            instance.save()
        return instance
