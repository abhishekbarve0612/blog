from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Comment
class CommentForm(forms.ModelForm):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    # content = forms.CharField(label = '', widget=forms.TextInput(attrs=
    #     {
    #         'cols' : 40,
    #         'rows' : 60,
    #     }
    # ))

    class Meta:
        model = Comment
        fields = ['content', 'content_type', 'object_id']


    