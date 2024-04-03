from django import forms
from .models import OverdoseForm
'''class ODForm(forms.Form):
    incident_number = forms.CharField(max_length= 20)
    ingestion_method = forms.CharField(max_length=100)
    source = forms.CharField(max_length=100)
    drug_type = forms.CharField(max_length=100)
    provider_safety = forms.CharField(max_length=100)
    narcan_usage = forms.CharField(max_length=100)
    interest_in_community_programs = forms.BooleanField(required=False)'''

from django import forms
from .models import OverdoseForm


class OverdoseFormForm(forms.ModelForm):
    ingestion_method = [
        ('oral', 'Oral'),
        ('injection', 'Injection'),
        ('inhalation', 'Inhalation'),
        ('snorting', 'Snorting'),
        ('other', 'Other'),
        ('smoking','smoking'),
        ('insuffation','insuffation'),
        ('sublingual','sublingual'),
        ('rectal','rectal'),
        ('transdermal','transdermal'),
        ('topical','topical'),
        ('intranasal','intranasal'),
        ('subcutaneous','subcutaneous')
        # Add more options as needed
    ]
    drug_type  = [
        ('Cannabis','Cannabis'),
         ('Stimulants','Stimulants'),
        ('Opioids','Opioids'),
        ('Hallucinogens','Hallucinogens'),
        ('Dissociatives','Dissociatives'),
        ('Sedatives','Sedatives'),
        ('Hypnotics','Hypnotics'),
        ('Anabolic Steroids','Anabolic Steroids'),
        ('Inhalants','Inhalants'),
        ('Designer Drugs','Designer Drugs'),
        ('Club Drugs','Club Drugs')

    ]
    source = [
        ('Marijuana', 'Marijuana'),
        ('Hashish', 'Hashish'),
        ('Synthetic cannabinoids', 'Synthetic cannabinoids'),
        ('nitrious', 'nitrious'),
        ('Cocaine', 'Cocaine'),
        ('Amphetamines', 'Amphetamines'),
        ('methamphetamine', 'Meth'),
        ('bath salts', 'bath salts'),
        ('crystamephetamie', 'crystamephetamine'),
        ('Heroin', 'Heroin'),
        ('Fentanyl','Fentanyl'),
        ('Opium', 'Opium'),
        ('Fentanyl', 'Fentanyl'),
        ('Krokodil', 'Kokodil'),
        ('LSD', 'LSD'),
        ('magic mushrooms', 'magic mushroom'),
        ('Peyote', 'Peyote'),
        ('mescaline', 'mescaline'),
        ('dimethyltryptamine', 'dimethylamine'),
        ('PCP', 'PCP'),
        ('angel dust', 'angel dust'),
        ('Ketamine special K', 'ketamine special K'),
        ('dextromethorphan', 'dextromethorphan'),
        ('Barbiturates', 'Barbiturates'),
        ('Benzodiazepines', 'Benzodiazepines'),
        ('GHB', 'GHB'),
        ('Anabolic Steroids', 'Anablic Steroids'),
        ('Nitrious', 'Nitrious'),
        ('gas', 'gas'),
        ('MDMA', 'MDMA'),
        ('Ecstasy', 'Ecstasy'),
        ('Rohypnol', 'Rohypnol'),
        ('Xylazine aka “Tranq', 'Xylazine aka Tranq'),
        ('Xanax', 'Xanax')
    ]




    ingestion_method = forms.ChoiceField(choices=ingestion_method)  # Override the 'route' field
    source = forms.ChoiceField(choices=source)
    drug_type  = forms.ChoiceField(choices=drug_type )
    class Meta:
        model = OverdoseForm
        fields = '__all__'  # includes all fields from the model
