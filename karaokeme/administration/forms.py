from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()

class UserForm(forms.ModelForm):
    """ ModelForm for Users.

    This is the general form for creating Users.

    Attributes
    ----------
    username = Username
        Username for the user to login into the system.
    email = Email
        Email required for the user, has format validation.
    password = Password
        Password for the user, the widget PasswordInput hides the characters in the field
    """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserLoginForm(forms.Form):
    """ Form for Login.

    This is the general form for logging in a User.

    Attributes
    ----------
    username = Username
        User's username.
    password = Password
        User's password, the widget PasswordInput hides the characters in the field
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # If the username or the password are incorrect, the user will not be logged in and ValitadionErrors will appear.  
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("The user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        # If both the username and the password are correct the user logs in. 
        return super(UserLoginForm, self).clean(*args, **kwargs)
