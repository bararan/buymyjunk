from django import forms
from .models import Item, Image
from django.utils.safestring import mark_safe
class PostItem(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('seller',)

class ImageWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None, *args, **kwargs):
        input_html = super().render(name, value, attrs={'id': 'image-input'}, **kwargs)
        if value is not None:
            img = value.instance
            # btn_html = mark_safe(f'<a class="btn btn-danger deleteImage" href="/images/{img.id}/delete">Delete</a>')
            identifier = f"delete_{img.id}"
            delete_check = mark_safe(f'''
            <div id="div_id_{identifier}" class="form-check">
                <input type="checkbox" name="{img.id}" class="delete-image" id="id_{identifier}"> 
                <label for="id_{identifier}" class="form-check-label">Delete</label>
            </div>
            ''')
            return f'{input_html}{delete_check}'
        else:
            return f'{input_html}'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ('item',)

ImageFormSet = forms.modelformset_factory(
    Image, 
    form=ImageForm,
    widgets={"image": ImageWidget}, 
    extra=6, 
    max_num=6
    )
