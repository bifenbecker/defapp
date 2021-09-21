from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(max_length=75, required=True,
                            widget=forms.EmailInput(attrs={'class': 'form-control form-control-user mt-3', 'placeholder': 'E-Mail адрес'}))
    password = forms.CharField(max_length=128, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user mt-3', 'placeholder': 'Пароль'}))
    confirm_password = forms.CharField(max_length=128, required=True,
                                       widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user mt-3', 'placeholder': 'Пароль (ещё раз)'}))

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['password'].label = ''
        self.fields['confirm_password'].label = ''

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(f"Аккаунт с таким адресом уже существует")

        if '@' not in email:
            raise forms.ValidationError("Неверный формат почты")

        return email

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")

        return self.cleaned_data


class LoginForm(AuthenticationForm):
    username = None
    email = forms.EmailField(max_length=75, required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-control-user mt-3', 'placeholder': 'Введите E-Mail адрес...'}))
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user mt-3', 'placeholder': 'Пароль', 'autocomplete': 'current-password'}),
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, username=email, email=email, password=password)
            if self.user_cache is None:
                raise ValidationError('Неверная почта и пароль', code='invalid_login')
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError('Аккаунт заблокирован', code='inactive')

    def get_user(self):
        return self.user_cache