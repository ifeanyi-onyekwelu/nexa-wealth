from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name", required=True)
    last_name = forms.CharField(max_length=30, label="Last Name", required=True)
    mobile = forms.CharField(max_length=15, label="Mobile", required=True)
    username = forms.CharField(max_length=15, label="Username", required=True)
    password1 = forms.CharField(
        max_length=128, label="Password", required=True, widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        max_length=128,
        label="Confirm Password",
        required=True,
        widget=forms.PasswordInput(),
    )

    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"]
        print(f"This is mobile: {mobile}")
        if User.objects.filter(mobile=mobile).exists():
            print("Mobile Already exists")
            raise ValidationError("A user with this mobile number already exists.")
        return mobile

    def save(self, request):
        print("Saving user...")
        print(f"Cleaned Data: {self.cleaned_data}")

        try:
            user = super(CustomSignupForm, self).save(request)
            print(f"User created: {user}")
        except Exception as e:
            print(f"Error before user save: {e}")
            raise e

        # Continue setting fields only if user creation succeeded
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.mobile = self.cleaned_data["mobile"]
        user.username = self.cleaned_data["username"]

        print(f"Before saving user details: {user}")
        user.save()
        print(f"User successfully saved: {user}")

        return user
