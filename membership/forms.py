from django import forms
from .models import Membership, MembershipType
from django.forms.widgets import DateInput


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        exclude = ('user', 'date', 'application_granted', )
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County, State or Locality',
            'postcode': 'Postal Code',
            'membership_type': 'Membership Type',
        }
