from django import forms
from .models import User
from datetime import date


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'age', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        date_of_birth = cleaned_data.get('date_of_birth')
        age = cleaned_data.get('age')

        if age <= 0:
            raise forms.ValidationError("Invalid Age.")
        print(date_of_birth.year)
        if date_of_birth.year >= 2020:
            raise forms.ValidationError("Date of birth should be less than 2020")

        if date_of_birth and age:
            today = date.today()

            user_age = today.year - date_of_birth.year - (
                        (today.month, today.day) < (date_of_birth.month, date_of_birth.day))

            if user_age != age or age <= 0:
                raise forms.ValidationError("Age does not match the date of birth.")

        return cleaned_data