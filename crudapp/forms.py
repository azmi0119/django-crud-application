from django import forms
from .models import Department, Employee


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "description"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),
        }


class EmployeeForm(forms.ModelForm):

    hobbies = forms.MultipleChoiceField(
        choices=Employee.HOBBY_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    gender = forms.ChoiceField(
        choices=Employee.GENDER_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Employee

        fields = [
            "name",
            "age",
            "email",
            "department",
            "profile_photo",
            "hobbies",
            "gender",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 18,
                    "max": 100,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "department": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
            "profile_photo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
        }

    def clean_age(self):
        age = self.cleaned_data["age"]

        if not 18 <= age <= 100:
            raise forms.ValidationError(
                "Age must be between 18 and 100."
            )

        return age

    def clean_profile_photo(self):
        photo = self.cleaned_data.get("profile_photo")

        if photo and photo.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "Photo must be 5 MB or smaller."
            )

        return photo