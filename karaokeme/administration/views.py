from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import View
from .forms import UserForm, UserLoginForm

class UserFormView(View):
    """ View for Creating Users.
    This view loads the form UserForm to create new users.

    """
    form_class = UserForm
    template_name = 'administration/registration_form.html'

    # Display a blank form 
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process form and data here
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # Storing locally the user but dont save it in the DB yet with commit=False
            # We need to normalize the data first
            user = form.save(commit=False)
            #Clean (normalize data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password) # whenever we need to change the user's 
            user.save() # Finally save the user

            # Return the User object if credentials are correct
            user = authenticate(username=username, password=password)
            
            # we log in the user
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # if we need to refer to the user logged in 'request.user'
                    messages.success(request, "Account succesfully created")
                    return redirect('songlibrary:list')

        return render(request, self.template_name, {'form': form})


def login_view(request):
    """ View for login.
    This view uses the UserLoginForm to login a user. 

    """
    # Check in console if a user is logged in, it should appear False first
    print(request.user.is_authenticated())
    form = UserLoginForm(request.POST or None)
    # The form's data is processed here
    if form.is_valid():
        # When the data has been processed (validated), the data is normalized with the cleaned_data.get() method
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        # Log in the user
        login(request, user)
        # At this point the console should return True since the user has successfully logged in
        print(request.user.is_authenticated())
        # Redirect to the list of petitions if the user is a Song Manager or an Admin
        if request.user.is_staff:
            messages.success(request, "User logged in")
            return redirect ('petition:list')
        # If a normal user logged in it is redirected to the Songlist
        else:
            messages.success(request, "User logged in")
            return redirect('songlibrary:list')
    return render(request, 'administration/login_form.html', {"form": form})


def logout_view(request):
    """ View for logout.
    This view calls the logout() method to logout the user
    and returns a feedback message to let know that the 
    user has logged out of the system.
    Finally it redirects to the login url.

    """
    logout(request)
    messages.success(request, "User logged out")
    return redirect('administration:login')
