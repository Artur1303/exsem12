from django import forms
from .models import Message


class MessangeForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text_message']