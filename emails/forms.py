from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter Your Name'
        }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter Your Email'
        }))