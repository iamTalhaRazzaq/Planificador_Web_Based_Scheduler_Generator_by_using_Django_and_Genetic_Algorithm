from cProfile import label
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    # username = forms.CharField(label="Please Enter your Username: ")
    password = forms.CharField(label='Passcode: ',widget=forms.PasswordInput)
    


class UserRegistrationForm(forms.ModelForm):

    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        label={'username':"User Id: ",
                'first_name':'Name: ',
                'email':"Enter Email: "
        }
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

