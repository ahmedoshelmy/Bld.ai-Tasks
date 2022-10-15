from django import forms
from .models import *


class AlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['approved'].help_text = "Approve the album if its name is not explicit"

    class Meta:
        model = Album
        exclude = ('',)
