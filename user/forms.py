from django import forms 

class auth(forms.Form):
    username=forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class registration(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
