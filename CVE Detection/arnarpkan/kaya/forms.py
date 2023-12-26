from django import forms
class Subscribe(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
