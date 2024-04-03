from django import forms

class MissingChildForm(forms.Form):
    full_name = forms.CharField(label='Full Name of Child', max_length=100)
    date_of_birth = forms.DateField(label='Date of Birth')
    last_seen_date = forms.DateTimeField(label='Date and Time Last Seen')
    last_seen_location = forms.CharField(label='Location Last Seen', max_length=200)
    description_of_clothing = forms.CharField(label='Description of Clothing Worn', max_length=200, required=False)
    physical_description = forms.CharField(label='Physical Description of Child', max_length=200)
    additional_information = forms.CharField(label='Any Additional Information', max_length=500, required=False)
    abductor_description = forms.CharField(label='Description of Abductor(s)', max_length=200, required=False)
    direction_of_travel = forms.CharField(label='Direction of Travel', max_length=100, required=False)
    contact_name = forms.CharField(label='Your Name', max_length=100)
    contact_phone = forms.CharField(label='Your Phone Number', max_length=15)
    contact_email = forms.EmailField(label='Your Email Address', required=False)
