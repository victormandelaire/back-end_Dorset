from django import forms
from .models import Tank


# creating a form
class TankForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = Tank

        # specify fields to be used
        fields = [
            "tankname",
            "nationality",
            "crewmates_num",
            "turret",
        ]