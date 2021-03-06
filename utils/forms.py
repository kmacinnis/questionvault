from django import forms
import re
from django.contrib.auth.models import User

FORM_INLINE = 'form-inline'
FORM_CONTROL = 'form-control'
INPUT_SIZE = 'input-sm'

CLASS_INLINE = {'class':FORM_INLINE}
CLASS_CONTROL = {'class':' '.join((FORM_CONTROL,INPUT_SIZE))}






class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
        )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput()
        )
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("""Username can only contain
                alphanumeric characters and the underscore.""")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')
