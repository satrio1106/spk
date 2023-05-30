from django.forms import ModelForm
from . models import Alternatif, BobotKriteria, Penilaian


class AlternatifForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override the default widget attributes with Bootstrap classes
        self.fields['name'].widget.attrs.update({'class': 'form-control w-75'})
        
    class Meta:
        model = Alternatif
        fields = ['name']

class BobotKriteriaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override the default widget attributes with Bootstrap classes
        self.fields['kriteria'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['bobot'].widget.attrs.update({'class': 'form-control w-75'})
    
    class Meta:
        model = BobotKriteria
        fields = '__all__'


class PenilaianForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override the default widget attributes with Bootstrap classes
        self.fields['alternatif'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['kelengkapan_fitur'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['kemudahan_penggunaan'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['keamanan'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['biaya'].widget.attrs.update({'class': 'form-control w-75'})


    class Meta:
        model = Penilaian
        fields = '__all__'