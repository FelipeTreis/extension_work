from collections import defaultdict

from django import forms

from app.models import Maintenance
from utils.django_forms import add_attr
from utils.strings import is_positive_number


class MaintenanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._errors = defaultdict(list)
        add_attr(self.fields.get('owner'), 'class', 'span-2')
        add_attr(self.fields.get('vehicle'), 'class', 'span-2')
        add_attr(self.fields.get('service'), 'class', 'span-2')
        add_attr(self.fields.get('km_vehicle'), 'class', 'span-2')

    class Meta:
        model = Maintenance
        fields = (
            'owner',
            'vehicle',
            'service',
            'km_vehicle',
        )

    def clean(self, request, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cleaned_data = self.cleaned_data
        owner = cleaned_data.get('owner')

        if owner != request.user:
            self._errors['owner'].append('Invalid owner, put your user')

        return super_clean

    def clean_km_vehicle(self):
        field_name = 'km_vehicle'
        field_value = self.cleaned_data.get(field_name)
        if not is_positive_number(field_value):
            self._errors[field_name].append('Must be a positive number')
        return field_value
