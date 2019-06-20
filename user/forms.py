
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

"""
 Here we are defining four fields namely username, email, password1 and password2; with their own clean_<field_name>() method (except for password1 field).
 Pay close attention to the widget keyword argument in both the password fields. The widget keyword argument allows us to change the default widget of the field.
 Recall that by default, CharField is rendered as text field (i.e <input type="text" ... >).
 To render the CharField as password field we have set widget keyword argument to forms.PasswordInput.

The clean_username() and clean_email() methods check for duplicate username and email respectively.
The clean_password2() method checks whether the password entered in both the fields matches or not. Finally, the save() method saves the data into the database.
"""
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150, help_text='Required. Inform a valid email address.')
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput,min_length=8, max_length=16)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput,min_length=8, max_length=16)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

"""
Notice that CustomUserCreationForm inherits from forms.Form class rather than forms.ModelForm.

"""
