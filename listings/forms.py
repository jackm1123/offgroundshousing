from django import forms

class MailForm(forms.Form):
    active = forms.BooleanField(required=False)



