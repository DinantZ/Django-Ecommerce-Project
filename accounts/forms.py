from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Въведи парола',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Потвърди парола',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder'] = 'Въведи първо име'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Въведи последно име'
            self.fields['username'].widget.attrs['placeholder'] = 'Въведи потребителско име'
            self.fields['phone_number'].widget.attrs['placeholder'] = 'Въведи телефонен номер'
            self.fields['email'].widget.attrs['placeholder'] = 'Въведи емейл адрес'
            for field in self.fields:
               self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Паролата не съвпада!"
            )