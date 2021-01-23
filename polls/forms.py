from django import forms
from .models import Poll


class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["name",'text','option1','option2','option3','option4','is_anon']  
    