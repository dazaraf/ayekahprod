# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:06:25 2020

@author: Alain Rosen
"""
from django import forms

class SignupForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter Your Name'
        }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter Your Email'
        }))


class LoginForm(forms.Form):
    username =  forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter Your username'
        }))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter Your password'
        }))
    
class RegisterForm(forms.Form):
    username =  forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter Your username'
        }))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter Your password'
        }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Confirm Your password'
        }))
    
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter Your email'
        }))
    
    def clean(self):
        
        data = self.cleaned_data
        password = data.get("password")
        password2 = data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Passwords don't match")
        else:
            return data