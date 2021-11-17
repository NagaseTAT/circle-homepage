from django import forms
from django.utils.encoding import force_bytes, force_text
# from .models import Post
#
class PostForm(forms.Form):
    labels = ['タグ']
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    tag = forms.MultipleChoiceField(
        label=labels[0],
        required=False,
        disabled=False,
        widget=forms.CheckboxSelectMultiple(attrs={
            'id': 'tag', 'class': 'form-check-input'}))
