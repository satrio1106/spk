from django.forms import ModelForm
from . models import Alternatif


class AlternatifForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override the default widget attributes with Bootstrap classes
        self.fields['name'].widget.attrs.update({'class': 'form-control w-75'})
        
    class Meta:
        model = Alternatif
        fields = ['name']
