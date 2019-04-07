from django import forms

class MailForm(forms.Form):
    active = forms.BooleanField(required=False)

class FavoriteForm(forms.Form):
    name = forms.CharField()
    favorite = forms.BooleanField(required=False)



