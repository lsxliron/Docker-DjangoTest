from django import forms

class modelForm(forms.Form):
	name = forms.CharField(max_length=20)
	phone = forms.CharField(max_length=20)
