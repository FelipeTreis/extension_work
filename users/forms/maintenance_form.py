from django import forms

from app.models import Maintenance
from utils.django_forms import add_attr


class MaintenanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
