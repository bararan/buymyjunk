from django import forms
from .models import Item, Image

class PostItem(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('seller',)
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ('item',)

ImageFormSet = forms.modelformset_factory(Image, form=ImageForm, extra=6, max_num=6)
''' TODO: Make it possible to delete images in this form.
'''